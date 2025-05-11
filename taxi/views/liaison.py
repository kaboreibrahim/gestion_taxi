from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView,UpdateView
from taxi.models import LiaisonVehiculeChauffeur,Vehicule,Chauffeur,Proprietaire
from taxi.forms import LiaisonVehiculeChauffeurForm
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator



@method_decorator(login_required, name='dispatch')
class LiaisonVehiculeChauffeurListView(ListView):
    model = LiaisonVehiculeChauffeur
    context_object_name = 'liaison_list'
    template_name = 'pages/liaison/liaison_list.html'
    paginate_by = 10  # Définit le nombre d'éléments par page

    def get_queryset(self):
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        queryset = LiaisonVehiculeChauffeur.objects.filter(proprietaire=proprietaire)
        return queryset


        

@method_decorator(login_required, name='dispatch')
class LiaisonVehiculeChauffeurCreateView(CreateView):
    model = LiaisonVehiculeChauffeur
    form_class = LiaisonVehiculeChauffeurForm
    template_name = 'pages/liaison/liaison_create.html'
    success_url = reverse_lazy('liaison_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    """def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrer les choix de véhicules et chauffeurs liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)

        form.fields['vehicule'].queryset = Vehicule.objects.filter(Proprietaire__user=user)
        form.fields['chauffeur'].queryset = Chauffeur.objects.filter(proprietaire__user=user)
        return form"""
    
    def form_valid(self, form):
        messages.success(self.request, "Liaison effectuée avec succès")
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.FILES)
        form = LiaisonVehiculeChauffeurForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.instance.proprietaire = self.request.user  # Assigner directement l'utilisateur connecté
            form.save()
            return HttpResponseRedirect(reverse('liaison_list'))
        else:
            print(form.errors)
            messages.error(request, "ERREUR !!! Une erreur s'est produite")
            return HttpResponseRedirect(reverse('liaison_create'))

    def get_form_valid_message(self):
        return u"{0} nouveau véhicule ajouté avec succès!".format(self.object.name)


    """ def form_invalid(self, form):
        messages.error(self.request, "ERREUR !!! Une erreur s'est produite")
        return super().form_invalid(form)"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context

@method_decorator(login_required, name='dispatch')
class LiaisonVehiculeChauffeurUpdateView(UpdateView):
    model = LiaisonVehiculeChauffeur
    form_class = LiaisonVehiculeChauffeurForm
    template_name = 'pages/liaison/liaison_create.html'
    success_url = reverse_lazy('liaison_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(LiaisonVehiculeChauffeur, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context