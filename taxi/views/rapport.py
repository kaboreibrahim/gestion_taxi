from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from taxi.models import (
    Proprietaire, Vehicule, Recette, Depense, Assurance, 
    VisiteTechnique, Notebook, Vidange
)
from django.db.models import Sum

@login_required
def rapport_vehicule(request):
    user = request.user
    # Récupérer le propriétaire lié à l'utilisateur connecté
    proprietaire = Proprietaire.objects.get(username=user.username)
    # Filtrer les véhicules en fonction du propriétaire
    vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

    if request.method == 'POST':
        # Récupérer l'identifiant du véhicule depuis la requête
        vehicule_id = request.POST.get('vehicule_id')
        vehicule = Vehicule.objects.get(id=vehicule_id)
        
        # Définir la période des 3 derniers mois
        trois_mois = timezone.now() - timezone.timedelta(days=90)

        # Filtrer les dépenses, assurances, visites techniques et recettes pour le véhicule sur les 3 derniers mois
        depenses = Depense.objects.filter(immatriculation=vehicule, Date_depense__gte=trois_mois)
        assurances = Assurance.objects.filter(immatriculation=vehicule, Date_ajout__gte=trois_mois)
        visitetechnique = VisiteTechnique.objects.filter(immatriculation=vehicule, Date_ajout__gte=trois_mois)
        recettes = Recette.objects.filter(immatriculation=vehicule, Date_ajout__gte=trois_mois)

        # Calculer les sommes des dépenses, assurances, visites techniques et recettes
        total_recettes = recettes.aggregate(Sum('Montant'))['Montant__sum'] or 0
        total_depenses = depenses.aggregate(Sum('Montant'))['Montant__sum'] or 0
        total_assurance = assurances.aggregate(Sum('Montant_Assurance'))['Montant_Assurance__sum'] or 0
        total_visitetechnique = visitetechnique.aggregate(Sum('Montant'))['Montant__sum'] or 0

        # Calculer le total des dépenses
        totals_depenses = total_depenses + total_assurance + total_visitetechnique
        print(totals_depenses)
        # Calculer le résultat net
        total = total_recettes - totals_depenses

        # Nombre de fois que le véhicule est parti au garage au cours des 3 derniers mois
        garages = Notebook.objects.filter(vehicule=vehicule, date_arrivage__gte=trois_mois).count()

        # Kilométrage à la dernière venue au garage et à la dernière vidange
        dernier_garage = Notebook.objects.filter(vehicule=vehicule).order_by('-date_arrivage').first()
        dernier_vidange = Vidange.objects.filter(immatriculation=vehicule).order_by('-Date_vidange').first()

        # Date de fin de l'assurance et de la visite technique
        assurance = Assurance.objects.filter(immatriculation=vehicule).order_by('-Date_fin').first()
        visite_technique = VisiteTechnique.objects.filter(immatriculation=vehicule).order_by('-Date_de_fin').first()

        # Dernière date de venue au garage
        derniere_date_garage = dernier_garage.date_arrivage if dernier_garage else None

        # Année d'ancienneté du véhicule
        annee_anciennete = timezone.now().year - vehicule.Date_mise_en_circulation.year

        context = {
            'vehicule': vehicule,
            'totals_depenses': totals_depenses,
            'total': total,
            'total_recettes': total_recettes,
            'garages': garages,
            'dernier_garage_km': dernier_garage.Kilometrage if dernier_garage else None,
            'dernier_vidange_km': dernier_vidange.Kilometrage_vidange if dernier_vidange else None,
            'assurance_fin': assurance.Date_fin if assurance else None,
            'visite_technique_fin': visite_technique.Date_de_fin if visite_technique else None,
            'derniere_date_garage': derniere_date_garage,
            'annee_anciennete': annee_anciennete,
        }

        return render(request, 'pages/rapport/rapport.html', context)

    # Si la méthode n'est pas POST, afficher le formulaire de sélection
    return render(request, 'pages/rapport/rapport.html', {'vehicules': vehicules})
