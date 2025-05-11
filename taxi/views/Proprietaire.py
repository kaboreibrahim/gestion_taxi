from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from taxi.models import Proprietaire, Vehicule

@login_required
def afficher_informations_proprietaire(request):
    user = request.user
    
    # Récupérer l'enregistrement Proprietaire correspondant à l'utilisateur
    try:
        proprietaire = Proprietaire.objects.get(user=user)
        nombre_vehicules = Vehicule.objects.filter(proprietaire=proprietaire).count()
    except Proprietaire.DoesNotExist:
        proprietaire = None
        nombre_vehicules = 0

    # Rendre les informations dans un modèle
    return render(request, 'pages/proprietaire/informations_proprietaire.html', {'proprietaire': proprietaire, 'nombre_vehicules': nombre_vehicules})
