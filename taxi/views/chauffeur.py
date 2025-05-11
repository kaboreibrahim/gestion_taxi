from taxi.models import Chauffeur,Proprietaire
from taxi.forms import ChauffeurForm
from django.views.generic import ListView,CreateView,UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy,reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator


def afficher_details_Chauffeur(request, detail_Chauffeur_id):
    detail_Chauffeur = get_object_or_404(Chauffeur, id=detail_Chauffeur_id)
    return render(request,"pages/Chauffeur/detail_chauffeur.html", {'detail_Chauffeur': detail_Chauffeur})


@method_decorator(login_required, name='dispatch')
class ChauffeurList(ListView):
    model = Chauffeur
    context_object_name = 'list_Chauffeur'
    template_name = 'pages/Chauffeur/list_Chauffeur.html'
    paginate_by = 10  # Définit le nombre d'éléments par page

    def get_queryset(self):
        # Filter the chauffeurs for the connected user (Proprietaire)
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        queryset = Chauffeur.objects.filter(proprietaire=proprietaire)

        
        return queryset




class ChauffeurCreateView(CreateView):
    model = Chauffeur
    form_class = ChauffeurForm
    template_name = 'pages/Chauffeur/create_Chauffeur.html'
    success_url = reverse_lazy('list_Chauffeur')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"{0} nouveau Chauffeur ajouté avec succès!".format(self.object.name)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.FILES)
        form = ChauffeurForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.proprietaire = self.request.user  # Assigner directement l'utilisateur connecté
            form.save()
            return HttpResponseRedirect(reverse('list_Chauffeur'))
        else:
            print(form.errors)
            messages.error(request, "ERREUR !!! Une erreur s'est produite")
            return HttpResponseRedirect(reverse('create_Chauffeur'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context

@method_decorator(login_required, name='dispatch')
class ChauffeurUpdateView(UpdateView):
    model = Chauffeur
    form_class = ChauffeurForm
    template_name = "pages/Chauffeur/create_Chauffeur.html"
    success_url = reverse_lazy('list_Chauffeur')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Chauffeur, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context