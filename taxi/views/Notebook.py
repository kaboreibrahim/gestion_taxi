from taxi.models import Notebook,Vehicule,Proprietaire,Chauffeur
from taxi.forms import NotebookForm
from django.views.generic import ListView,CreateView,UpdateView
from braces.views import FormMessagesMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy,reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect
from django.contrib import messages
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from django.http import JsonResponse




@method_decorator(login_required, name='dispatch')
class NotebookList(ListView):
    model = Notebook
    context_object_name = 'Notebook_List'
    template_name = 'pages/Notebook/list_Notebook.html'
   
    def get_queryset(self):
        user = self.request.user
        # Récupérer le propriétaire lié à l'utilisateur connecté
        proprietaire = Proprietaire.objects.get(username=user.username)
        # Filtrer les véhicules en fonction du propriétaire
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)
        # Filtrer les Notebook en fonction des véhicules filtrés
        queryset = Notebook.objects.filter(vehicule__in=vehicules ,statut_vehicule = 'garage')

        return queryset




@login_required
def vehicule_list(request):


    user = request.user
    # Récupérer le propriétaire lié à l'utilisateur connecté
    proprietaire = Proprietaire.objects.get(username=user.username)
    # Filtrer les véhicules en fonction du propriétaire
    vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)
    return render(request, 'pages/Notebook/vehicule_list.html', {'vehicules': vehicules})
    

def vehicule_detail(request, vehicule_id):
    vehicule = get_object_or_404(Vehicule, id=vehicule_id)
    notebook = Notebook.objects.filter(vehicule=vehicule)
    return render(request, 'pages/Notebook/vehicule_detail.html', {'vehicule': vehicule, 'notebook': notebook})



def change_statut_to_circulation(request, notebook_id):
    notebook = get_object_or_404(Notebook, id=notebook_id)
    notebook.change_statut_to_circulation()
    return redirect('vehicule_detail', vehicule_id=notebook.vehicule.id)

        
@method_decorator(login_required, name='dispatch')
class NotebookCreateView(CreateView):
    model = Notebook
    form_class = NotebookForm
    template_name = 'pages/Notebook/create_Notebook.html'
    success_url = reverse_lazy('Notebook_List')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrer les choix de véhicules liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        form.fields['piece'].queryset = proprietaire.piece_set.all()

        form.fields['vehicule'].queryset =proprietaire.vehicule_set.all()
        #form.fields['chauffeur'].queryset = proprietaire.chauffeurs.all()
        return form

    def get_form_valid_message(self):
        return "Nouvelle Notebook ajoutée avec succès!"

    def form_valid(self, form):
        messages.success(self.request, "Ajout de la nouvelle Notebook dans la base de données")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ERREUR !!! Une erreur s'est produite")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context

def load_chauffeurs(request):
    vehicule_id = request.GET.get('vehicule_id')
    chauffeurs = Chauffeur.objects.filter(liaisonvehiculechauffeur__vehicule_id=vehicule_id).distinct()
    return JsonResponse(list(chauffeurs.values('id', 'Nom', 'Prenom')), safe=False)

@method_decorator(login_required, name='dispatch')
class NotebookUpdateView(UpdateView):
    model = Notebook
    form_class = NotebookForm
    template_name = 'pages/Notebook/create_Notebook.html'
    success_url = reverse_lazy('Notebook_List')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return "Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Notebook, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context

    def form_valid(self, form):
        # Convertir les tâches en JSON avant de sauvegarder
        form.instance.commentaire = form.cleaned_data['commentaire']
        return super().form_valid(form)
    
  