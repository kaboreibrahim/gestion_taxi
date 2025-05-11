from urllib import request
from taxi.models import Proprietaire, Recette,Vehicule
from taxi.forms import recetteForm
from django.views.generic import ListView,CreateView,UpdateView,View
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy,reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect
from django.contrib import messages
from django.db.models import Sum
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core.paginator import Paginator

@method_decorator(login_required, name='dispatch')
class RecetteDetails(ListView):
    model = Recette
    template_name = 'pages/recette/detail_recette_vehicule.html'
    context_object_name = 'recettes'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtrer les recettes en fonction du véhicule sélectionné
        vehicule_id = self.request.GET.get('vehicule_id')
        if vehicule_id:
            queryset = queryset.filter(immatriculation_id=vehicule_id)

        # Filtrer les recettes en fonction des dates sélectionnées
        date_debut = self.request.GET.get('date_debut')
        date_fin = self.request.GET.get('date_fin')

        if date_debut and date_fin:
            date_fin = datetime.strptime(date_fin, '%Y-%m-%d') + timedelta(days=1)
            date_fin = date_fin.strftime('%Y-%m-%d')
            queryset = queryset.filter(Date_ajout__range=(date_debut, date_fin))
      
        return queryset
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupérer le propriétaire associé à l'utilisateur connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        # Récupérer les véhicules associés au propriétaire
        context['vehicules'] = Vehicule.objects.filter(Proprietaire=proprietaire)
        # Calculer le total des recettes pour le véhicule sélectionné
        vehicule_id = self.request.GET.get('vehicule_id')
        if vehicule_id:
            # Récupérer les recettes pour le véhicule sélectionné
            recettes = self.get_queryset()
            # Calculer le total des recettes
            total_recette = recettes.aggregate(Sum('Montant'))
            context['total_recette'] = total_recette['Montant__sum'] if total_recette['Montant__sum'] else 0
            # Récupérer les données pour le graphique
            data = [{'Date_ajout': recette.Date_ajout.strftime('%Y-%m-%d'), 'Montant': recette.Montant} for recette in recettes]
            context['graph_data'] = data
        return context


@method_decorator(login_required, name='dispatch')
class RecetteList(ListView):
    model = Recette
    context_object_name = 'list_recette'
    template_name = 'pages/recette/list_recette.html'
    paginate_by = 10  # Définit le nombre d'éléments par page

    
    def get_queryset(self):
        # Get the logged-in user
        user = self.request.user
        
        # Get the Proprietaire instance associated with the logged-in user
        proprietaire = Proprietaire.objects.get(username=user.username)
        
        # Filter vehicles linked to the logged-in user
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

        # Récupérer les paramètres de date de début et de fin à partir de la requête
        start_date = self.request.GET.get('date_debut')
        end_date = self.request.GET.get('date_fin')
         # Ajouter un jour à la date de fin
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
            end_date = end_date.strftime('%Y-%m-%d')

    
        # Filter Recette objects based on the vehicles associated with the user
        queryset = Recette.objects.filter(immatriculation__in=vehicules)
            # Filtrer les transferts en fonction des dates de début et de fin
        if start_date and end_date:
            
            queryset = queryset.filter(Date_ajout__range=(start_date, end_date))
            
        queryset = queryset.order_by('-Date_ajout')
        
        return queryset

@method_decorator(login_required, name='dispatch')

class RecetteCreateView(CreateView):
    model = Recette
    form_class = recetteForm
    template_name = 'pages/recette/create_recette.html'
    success_url = reverse_lazy('list_recette')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrer les choix de véhicules liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        form.fields['immatriculation'].queryset = proprietaire.vehicule_set.all()
        return form

    def get_form_valid_message(self):
        
        return "Nouvelle recette ajoutée avec succès!"

    def form_valid(self, form):
        messages.success(self.request, "Ajout de la nouvelle recette dans la base de données")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ERREUR !!! Une erreur s'est produite")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context
    
@method_decorator(login_required, name='dispatch')
class RecetteUpdateView(UpdateView):
    model = Recette
    form_class = recetteForm
    template_name = 'pages/recette/create_recette.html'
    success_url = reverse_lazy('list_recette')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Recette, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context