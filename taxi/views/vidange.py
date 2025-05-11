from taxi.models import Vidange,Proprietaire
from taxi.forms import VidangeForm
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
def afficher_details_Vidange(request, detail_Vidange_id):
    detail_Vidange = get_object_or_404(Vidange, id=detail_Vidange_id)
    return render(request,"pages/Vidange/detail_Vidange.html", {'detail_Vidange': detail_Vidange})

class VidangeList(ListView):
    model = Vidange
    context_object_name = 'list_Vidange'
    paginate_by = 10  # Définit le nombre d'éléments par page
    template_name = 'pages/Vidange/list_Vidange.html'

    def get_queryset(self):
        # Récupérer l'utilisateur connecté
        user = self.request.user
        # Filtrer les véhicules liés au propriétaire connecté         
        proprietaire = Proprietaire.objects.get(username=user.username)

        vehicules_proprietaire = proprietaire.vehicule_set.all()

        # Filtrer les vidanges en fonction des véhicules liés au propriétaire connecté
        queryset = Vidange.objects.filter(immatriculation__in=vehicules_proprietaire)

        # Filtrer les vidanges en fonction des dates sélectionnées
        date_debut = self.request.GET.get('date_debut')
        date_fin = self.request.GET.get('date_fin')

        if date_debut and date_fin:
            date_fin = datetime.strptime(date_fin, '%Y-%m-%d') + timedelta(days=1)
            date_fin = date_fin.strftime('%Y-%m-%d')
            queryset = queryset.filter(Date_vidange__range=(date_debut, date_fin))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vidanges_grouped_by_immatriculation = {}
        for vidange in context['list_Vidange']:
            immatriculation = vidange.immatriculation
            if immatriculation not in vidanges_grouped_by_immatriculation:
                vidanges_grouped_by_immatriculation[immatriculation] = []
            vidanges_grouped_by_immatriculation[immatriculation].append({
                'vidange': vidange,
                'vehicule_image_url': vidange.get_vehicule_image_url()
            })
        context['vidanges_grouped_by_immatriculation'] = vidanges_grouped_by_immatriculation
        return context


        
class VidangeCreateView(CreateView):
    model = Vidange
    form_class = VidangeForm
    template_name = 'pages/Vidange/create_Vidange.html'
    success_url = reverse_lazy('list_Vidange')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if form is None:
            raise ValueError("Form is None")
        # Filtrer les choix de véhicules liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)

        form.fields['immatriculation'].queryset = proprietaire.vehicule_set.all()
        form.fields['Nom_chauffeur'].queryset = proprietaire.chauffeurs.all()
        return form
    
    def get_form_valid_message(self):
        return "Nouvelle vidange ajoutée avec succès!"

    def form_valid(self, form):
        messages.success(self.request, "Ajout de la nouvelle vidange dans la base de données")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ERREUR !!! Une erreur s'est produite")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        context['form'] = self.get_form()  # Assurez-vous que le formulaire est ajouté au contexte
        return context



@method_decorator(login_required, name='dispatch')
class VidangeUpdateView(UpdateView):
    model = Vidange
    form_class = VidangeForm
    template_name = "pages/Vidange/create_Vidange.html"
    success_url = reverse_lazy('list_Vidange')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Vidange, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context