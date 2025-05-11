from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from taxi.forms import ModeleDeVoitureForm
from taxi.models import ModeleDeVoiture
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from braces.views import FormMessagesMixin
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.core.paginator import Paginator


@method_decorator(login_required, name='dispatch')
class ModeleDeVoitureListView(ListView):
    """
        vue d'affichage de la liste des projects
    """
    model = ModeleDeVoiture
    context_object_name = 'ModeleDeVoiture_list'
    template_name = "pages/ModeleDeVoiture/list_ModeleDeVoiture.html"
    paginate_by = 10  # Définit le nombre d'éléments par page



    def get_queryset(self):
        user = self.request.user
        queryset = ModeleDeVoiture.objects.filter(Proprietaire=user)
        return queryset


   
@method_decorator(login_required, name='dispatch')
class ModeleDeVoitureCreateView(FormMessagesMixin, CreateView):
    """
      Vue de création d'un ModeleDeVoiture
    """
    model = ModeleDeVoiture
    form_class = ModeleDeVoitureForm
    template_name = "pages/ModeleDeVoiture/ModeleDeVoiture_create.html"
    success_url = reverse_lazy('ModeleDeVoiture_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    
    def get_form_valid_message(self):
        return u"nouveau ModeleDeVoiture ajouté avec succès!"

    def form_valid(self, form):
        form.instance.Proprietaire = self.request.user  # assignez le propriétaire connecté au nouveau véhicule
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # transmettez l'utilisateur connecté au formulaire
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context

    

@method_decorator(login_required, name='dispatch')
class ModeleDeVoitureUpdateView(UpdateView):
    model = ModeleDeVoiture
    form_class = ModeleDeVoitureForm
    template_name = "pages/ModeleDeVoiture/ModeleDeVoiture_create.html"
    success_url = reverse_lazy('ModeleDeVoiture_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(ModeleDeVoiture, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context
    

def afficher_details_ModeleDeVoiture(request, detail_ModeleDeVoiture_id):
    detail_ModeleDeVoiture = get_object_or_404(ModeleDeVoiture, id=detail_ModeleDeVoiture_id)
    return render(request,"pages/ModeleDeVoiture/detail_ModeleDeVoiture.html", {'detail_ModeleDeVoiture': detail_ModeleDeVoiture})