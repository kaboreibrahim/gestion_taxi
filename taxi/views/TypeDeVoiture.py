from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from taxi.forms import TypeDeVoitureForm
from taxi.models import TypeDeVoiture
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from braces.views import FormMessagesMixin
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.core.paginator import Paginator


@method_decorator(login_required, name='dispatch')
class TypeDeVoitureListView(ListView):
    """
        vue d'affichage de la liste des projects
    """
    model = TypeDeVoiture
    context_object_name = 'TypeDeVoiture_list'
    template_name = "pages/TypeDeVoiture/list_TypeDeVoiture.html"
    paginate_by = 10  # Définit le nombre d'éléments par page



    def get_queryset(self):
        user = self.request.user
        queryset = TypeDeVoiture.objects.filter(Proprietaire=user)
        return queryset


@method_decorator(login_required, name='dispatch')
class TypeDeVoitureCreateView(FormMessagesMixin, CreateView):
    """
    Vue de création d'un TypeDeVoiture
    """
    model = TypeDeVoiture
    form_class = TypeDeVoitureForm
    template_name = "pages/TypeDeVoiture/TypeDeVoiture_create.html"
    success_url = reverse_lazy('TypeDeVoiture_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"{0} crée avec succès!".format(self.object.title)

    def post(self, request, *args, **kwargs):
        print(f"Project Post : {request.POST}")
        form = TypeDeVoitureForm(request.POST)
        if form.is_valid():
            form.instance.Proprietaire = self.request.user  # Assigner directement l'utilisateur connecté
            form.save()
            return HttpResponseRedirect(reverse('TypeDeVoiture_list'))
        else:
            print(f"Project form errors : {form.errors}")
            return render(request, self.template_name, {"form": form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TypeDeVoitureForm()
        context['method'] = "post"
        return context

@method_decorator(login_required, name='dispatch')
class TypeDeVoitureUpdateView(UpdateView):
    model = TypeDeVoiture
    form_class = TypeDeVoitureForm
    template_name = "pages/TypeDeVoiture/TypeDeVoiture_create.html"
    success_url = reverse_lazy('TypeDeVoiture_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(TypeDeVoiture, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context
    

def afficher_details_TypeDeVoiture(request, detail_TypeDeVoiture_id):
    detail_TypeDeVoiture = get_object_or_404(TypeDeVoiture, id=detail_TypeDeVoiture_id)
    return render(request,"pages/TypeDeVoiture/detail_TypeDeVoiture.html", {'detail_TypeDeVoiture': detail_TypeDeVoiture})