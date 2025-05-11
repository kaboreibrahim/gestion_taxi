from taxi.models import CarteStationnement, Proprietaire,Vehicule
from taxi.forms import CarteStationnementForm
from django.views.generic import ListView,CreateView,UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy,reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect
from django.contrib import messages
from datetime import datetime, timedelta
from django.core.paginator import Paginator


def afficher_details_CarteStationnement(request, detail_CarteStationnement_id):
    detail_CarteStationnement = get_object_or_404(CarteStationnement, id=detail_CarteStationnement_id)
    return render(request,"pages/CarteStationnement/detail_CarteStationnement.html", {'detail_CarteStationnement': detail_CarteStationnement})

@method_decorator(login_required, name='dispatch')
class CarteStationnementList(ListView):
    model = CarteStationnement
    context_object_name = 'list_CarteStationnement'
    template_name = 'pages/CarteStationnement/list_CarteStationnement.html'
    paginate_by = 10  # Définit le nombre d'éléments par page

    def get_queryset(self):

        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)

        # Filter vehicles linked to the logged-in user
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

        queryset = CarteStationnement.objects.filter(immatriculation__in=vehicules)

        # Filtrer les CarteStationnements en fonction des dates sélectionnées
        date_debut = self.request.GET.get('date_debut')
        date_fin = self.request.GET.get('date_fin')

        if date_debut and date_fin:
            date_fin = datetime.strptime(date_fin, '%Y-%m-%d') + timedelta(days=1)
            date_fin = date_fin.strftime('%Y-%m-%d')
            queryset = queryset.filter(Date_ajout__range=(date_debut, date_fin))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        CarteStationnements_grouped_by_immatriculation = {}
        for CarteStationnement in context['list_CarteStationnement']:
            immatriculation = CarteStationnement.immatriculation
            if immatriculation not in CarteStationnements_grouped_by_immatriculation:
                CarteStationnements_grouped_by_immatriculation[immatriculation] = []
            CarteStationnements_grouped_by_immatriculation[immatriculation].append({
                'CarteStationnement': CarteStationnement,
                'vehicule_image_url': CarteStationnement.get_vehicule_image_url()
            })
        context['CarteStationnements_grouped_by_immatriculation'] = CarteStationnements_grouped_by_immatriculation
        return context



class CarteStationnementCreateView(CreateView):
    model = CarteStationnement
    form_class = CarteStationnementForm
    template_name = 'pages/CarteStationnement/create_CarteStationnement.html'
    success_url = reverse_lazy('list_CarteStationnement')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrer les choix de véhicules liés au propriétaire connecté
         # Filtrer les choix de véhicules liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        form.fields['immatriculation'].queryset = proprietaire.vehicule_set.all()
        return form


    def get_form_valid_message(self):
        return "Nouvelle CarteStationnement ajoutée avec succès!"

    def form_valid(self, form):
        messages.success(self.request, "Ajout de la nouvelle CarteStationnement dans la base de données")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ERREUR !!! Une erreur s'est produite")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context


@method_decorator(login_required, name='dispatch')
class CarteStationnementUpdateView(UpdateView):
    model = CarteStationnement
    form_class = CarteStationnementForm
    template_name = "pages/CarteStationnement/create_CarteStationnement.html"
    success_url = reverse_lazy('list_CarteStationnement')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(CarteStationnement, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context