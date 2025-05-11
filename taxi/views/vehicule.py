from taxi.models import Vehicule,Proprietaire
from taxi.forms import VehiculeForm
from django.views.generic import ListView,CreateView,UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy,reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator

def afficher_details_vehicule(request, detail_vehicule_id):
    detail_vehicule = get_object_or_404(Vehicule, id=detail_vehicule_id)
    return render(request,"pages/vehicule/detail_voiture.html", {'detail_vehicule': detail_vehicule})

@method_decorator(login_required, name='dispatch')

class VehiculeList(ListView):
    model = Vehicule
    context_object_name = 'list_voiture'
    template_name = 'pages/vehicule/list_Vehicule.html'
    paginate_by = 7  # Définit le nombre d'éléments par page

    def get_queryset(self):
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        queryset = Vehicule.objects.filter(Proprietaire=proprietaire).order_by('Date_mise_en_circulation')
        return queryset

class VehiculeCreateView(CreateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = 'pages/vehicule/create_Vehicule.html'
    success_url = reverse_lazy('list_voiture')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"{0} nouveau véhicule ajouté avec succès!".format(self.object.name)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrer les choix de véhicules liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)

        form.fields['Marque_voiture'].queryset =proprietaire.typedevoiture_set.all()
        form.fields['Modele_voiture'].queryset = proprietaire.modeledevoiture_set.all()
       
        return form
    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.FILES)
        form = VehiculeForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.Proprietaire = self.request.user  # Assigner directement l'utilisateur connecté
            form.save()
            return HttpResponseRedirect(reverse('list_voiture'))
        else:
            print(form.errors)
            messages.error(request, "ERREUR !!! Une erreur s'est produite")
            return HttpResponseRedirect(reverse('create_Vehicule'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context
    
    

@method_decorator(login_required, name='dispatch')
class VehiculeUpdateView(UpdateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = "pages/vehicule/create_Vehicule.html"
    success_url = reverse_lazy('list_voiture')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Vehicule, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['instance'] = self.object
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context
   