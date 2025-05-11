from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from taxi.models import Proprietaire, Vehicule, Recette, Depense,Assurance,VisiteTechnique,Notebook, Vidange, VisiteTechnique, Notebook
from datetime import datetime, timedelta
from django.db.models import Count,Sum




def get_french_month_name(month_number):
    """
    Renvoie le nom du mois en français en fonction du numéro du mois.
    """
    french_month_names = [
        "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre"
    ]
    return french_month_names[month_number - 1]

@login_required
def index(request, month=None):
    messages.add_message(request, messages.SUCCESS, "Bienvenue %s  " % request.user.username)

    user = get_user(request)
    proprietaire = Proprietaire.objects.get(username=user.username)
    vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

    # Récupérer les données pour le mois en cours
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    french_month_name = get_french_month_name(current_month)
    recettes = Recette.objects.filter(immatriculation__in=vehicules, Date_ajout__year=current_year, Date_ajout__month=current_month)
    depenses = Depense.objects.filter(immatriculation__in=vehicules, Date_ajout__year=current_year, Date_ajout__month=current_month)
    assurance = Assurance.objects.filter(immatriculation__in=vehicules, Date_ajout__year=current_year, Date_ajout__month=current_month)
    visitetechnique =VisiteTechnique.objects.filter(immatriculation__in=vehicules, Date_ajout__year=current_year, Date_ajout__month=current_month)

    total_recettes = recettes.aggregate(Sum('Montant'))['Montant__sum'] or 0
    total_depenses = depenses.aggregate(Sum('Montant'))['Montant__sum'] or 0
    total_assurance = assurance.aggregate(Sum('Montant_Assurance'))['Montant_Assurance__sum'] or 0
    total_visitetechnique = visitetechnique.aggregate(Sum('Montant'))['Montant__sum'] or 0
    

    totals_depenses=total_depenses+total_assurance+total_visitetechnique
    total = total_recettes - totals_depenses
    
    # Récupérer l'année sélectionnée à partir des données GET
    selected_year = request.GET.get('year')
    # Récupérer les données des recettes et dépenses pour les véhicules liés à l'utilisateur connecté
    recettes = Recette.objects.filter(immatriculation__in=vehicules)
    depenses = Depense.objects.filter(immatriculation__in=vehicules)
    assurance = Assurance.objects.filter(immatriculation__in=vehicules)
    visitetechnique =VisiteTechnique.objects.filter(immatriculation__in=vehicules)

    # Récupérer les années uniques pour les recettes et dépenses
    years = Recette.objects.values_list('Date_ajout__year', flat=True).distinct().order_by('-Date_ajout__year')

    # Créer un dictionnaire vide pour stocker les données des recettes et dépenses pour chaque année
    chart_data = {}

    # Parcourir les années et récupérer les données des recettes et dépenses pour chaque année
    for year in years:
        recettes_data = recettes.filter(Date_ajout__year=year).values('Date_ajout__month').annotate(total=Sum('Montant')).order_by('Date_ajout__month')
        depenses_data = depenses.filter(Date_ajout__year=year).values('Date_ajout__month').annotate(total=Sum('Montant')).order_by('Date_ajout__month')
        assurance_data = assurance.filter(Date_ajout__year=year).values('Date_ajout__month').annotate(total=Sum('Montant_Assurance')).order_by('Date_ajout__month')
        visitetechnique_data = visitetechnique.filter(Date_ajout__year=year).values('Date_ajout__month').annotate(total=Sum('Montant')).order_by('Date_ajout__month')
        # Créer une liste vide pour stocker les données des recettes et dépenses pour chaque mois de l'année
        recettes_months = [0] * 12
        depenses_months = [0] * 12
        benefice_months = [0] * 12
        
        # Parcourir les données des recettes et dépenses et mettre à jour les valeurs pour chaque mois
        for recette in recettes_data:
            recettes_months[recette['Date_ajout__month'] - 1] = recette['total']

        for depense in depenses_data:
            depenses_months[depense['Date_ajout__month'] - 1] = depense['total']
            
            # Ajouter les montants d'assurance aux dépenses
        for assurance in assurance_data:
            depenses_months[assurance['Date_ajout__month'] - 1] += assurance['total']
        
        # Ajouter les montants de visite technique aux dépenses
        for visite in visitetechnique_data:
            depenses_months[visite['Date_ajout__month'] - 1] += visite['total']
        print(f'total depense {depenses_months}')
        # Calculer le bénéfice pour chaque mois
        for i in range(12):
            benefice_months[i] = recettes_months[i] - depenses_months[i]

        # Ajouter les données des recettes et dépenses pour l'année au dictionnaire
        chart_data[year] = {
            'labels': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
            'datasets': [{
                'label': 'Recettes',
                'data': recettes_months,
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            }, {
                'label': 'Dépenses',
                'data': depenses_months,
                'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            }, {
                'label': 'Bénéfice',
                'data': benefice_months,
                'backgroundColor': 'rgba(0, 128, 0, 0.2)',  # vert clair transparent
                'borderColor': 'rgba(0, 128, 0, 1)',  # vert foncé opaque
                'borderWidth': 1
            }]
        }
        
    # Récupérer les données des recettes et dépenses pour l'année en cours
    recettes_annee = Recette.objects.filter(immatriculation__in=vehicules, Date_ajout__year=current_year)
    depenses_annee = Depense.objects.filter(immatriculation__in=vehicules, Date_ajout__year=current_year)
    assurance = Assurance.objects.filter(immatriculation__in=vehicules, Date_ajout__year=current_year)
    visitetechnique =VisiteTechnique.objects.filter(immatriculation__in=vehicules, Date_ajout__year=current_year)

    # Récupérer toutes les dépenses de l'année en cours
    total_depenses_annee = depenses_annee.aggregate(Sum('Montant'))['Montant__sum'] or 0

    # Récupérer toutes les recettes de l'année en cours
    total_recettes_annee = recettes_annee.aggregate(Sum('Montant'))['Montant__sum'] or 0
    
    total_assurance_annee = assurance.aggregate(Sum('Montant_Assurance'))['Montant_Assurance__sum'] or 0
    
    
    total_visitetechnique_annee = visitetechnique.aggregate(Sum('Montant'))['Montant__sum'] or 0
    
    total_depenses_annuel=total_depenses_annee+total_assurance_annee+total_visitetechnique_annee
    # Calculer le bénéfice de l'année en cours
    benefice_anne = total_recettes_annee - total_depenses_annuel
    
    ########################################    
    # Nombre de véhicules dans chaque statut
    status_counts = Notebook.objects.values('statut_vehicule').annotate(count=Count('id'))

    nombre_vehicules_au_garage = next((item['count'] for item in status_counts if item['statut_vehicule'] == 'garage'), 0)
    nombre_vehicules = Vehicule.objects.filter(Proprietaire=proprietaire).count()

    nombre_vehicules_en_circulation = nombre_vehicules-nombre_vehicules_au_garage
    ########################################  
    ########################################  les assurance de mon dashbord     ########################################  

    proprietaire = Proprietaire.objects.get(username=user.username)
    vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)
    today = timezone.now().date()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    assurances_queryset = Assurance.objects.filter(immatriculation__in=vehicules, Date_fin__range=(today, week_end)).order_by('Date_fin')

    
     # Calculer le nombre de jours restants pour chaque assurance
    assurances = []
    for assurance in assurances_queryset:
        jours_restants = (assurance.Date_fin - today).days
        assurances.append({
            'assurance': assurance,
            'jours_restants': jours_restants
        })

    ########################################  
    ########################################  les visites techinque de mon dashbord     ########################################  
    proprietaire = Proprietaire.objects.get(username=user.username)
    vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)
    today = timezone.now().date()

      # Récupère le premier et le dernier jour du mois en cours
    first_day_of_month = today.replace(day=1)
    if today.month == 12:
        last_day_of_month = today.replace(day=31)
    else:
        next_month = today.replace(month=today.month + 1, day=1)
        last_day_of_month = next_month - timezone.timedelta(days=1)

    queryset = VisiteTechnique.objects.filter(
        immatriculation__in=vehicules,
        Date_de_fin__range=[first_day_of_month, last_day_of_month]
    ).order_by('Date_de_fin')

    # Calculer le nombre de jours restants pour chaque visite technique
    visites_techniques = []
    for visite in queryset:
        jours_restants = (visite.Date_de_fin - today).days
        visites_techniques.append({
            'visite': visite,
            'jours_restants': jours_restants
        })


        
        
    """ # Étape 1 : Compter les visites au garage pour chaque véhicule
    vehicle_visits = (
        Notebook.objects.filter(statut_vehicule='garage')
        .values('vehicule')
        .annotate(garage_visits=Count('id'))
        .order_by('-garage_visits')[:5]
    )

    # Étape 2 : Récupérer les informations des véhicules
    top_5_vehicles_ids = [visit['vehicule'] for visit in vehicle_visits]

    # Étape 3 : Joindre les modèles pour obtenir les informations complètes
    top_5_vehicles = (
        Vehicule.objects.filter(id__in=top_5_vehicles_ids)
        .select_related('Modele_voiture', 'Marque_voiture')
        .values('immatriculation', 'Modele_voiture__nom', 'Marque_voiture__nom')
    )
    # Résultats
    print(f"Nombre de véhicules au garage: {nombre_vehicules_au_garage}")
    print(f"Nombre de véhicules en circulation: {nombre_vehicules_en_circulation}")
    print("Top 5 des véhicules qui vont le plus au garage:")
    for vehicle in top_5_vehicles:
        print(f"Immatriculation: {vehicle['immatriculation']}, Modèle: {vehicle['Modele_voiture__nom']}, Type: {vehicle['Marque_voiture__nom']}")
    """

    # Passer le dictionnaire au modèle HTML via le contexte du rendu
    return render(request, 'index.html', {
        'total_recettes': total_recettes,
        'totals_depenses': totals_depenses,
        'total': total,
        'chart_data': chart_data,
        'years': years,
        'selected_year': selected_year,
        'french_month_name': french_month_name,
        'total_depenses_annuel': total_depenses_annuel,
        'total_recettes_annee': total_recettes_annee,
        'benefice_anne': benefice_anne,
        'current_year': current_year,
        'proprietaire': proprietaire ,
        'nombre_vehicules_en_circulation':nombre_vehicules_en_circulation,
        'nombre_vehicules_au_garage':nombre_vehicules_au_garage,
        'nombre_vehicules':nombre_vehicules,
        'assurances': assurances,
        'visites_techniques': queryset,
        'today': today,
        #'top_5_vehicles': top_5_vehicles,
    })





