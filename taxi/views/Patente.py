from taxi.models import Patente, Proprietaire,Vehicule
from taxi.forms import PatenteForm
from django.views.generic import ListView,CreateView,UpdateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta
from django.core.paginator import Paginator


def afficher_details_Patente(request, detail_Patente_id):
    detail_Patente = get_object_or_404(Patente, id=detail_Patente_id)
    return render(request,"pages/Patente/detail_Patente.html", {'detail_Patente': detail_Patente})

@method_decorator(login_required, name='dispatch')
class PatenteList(ListView):
    model = Patente
    context_object_name = 'list_Patente'
    template_name = 'pages/Patente/list_Patente.html'
    paginate_by = 10  # Définit le nombre d'éléments par page

    def get_queryset(self):

        # Get the logged-in user
        user = self.request.user

        # Get the Proprietaire instance associated with the logged-in user
        proprietaire = Proprietaire.objects.get(username=user.username)

        # Filter vehicles linked to the logged-in user
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

        queryset = Patente.objects.filter(immatriculation__in=vehicules)

        # Filtrer les Patentes en fonction des dates sélectionnées
        date_debut = self.request.GET.get('date_debut')
        date_fin = self.request.GET.get('date_fin')

        if date_debut and date_fin:
            date_fin = datetime.strptime(date_fin, '%Y-%m-%d') + timedelta(days=1)
            date_fin = date_fin.strftime('%Y-%m-%d')
            queryset = queryset.filter(Date_ajout__range=(date_debut, date_fin))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Patentes_grouped_by_immatriculation = {}
        for Patente in context['list_Patente']:
            immatriculation = Patente.immatriculation
            if immatriculation not in Patentes_grouped_by_immatriculation:
                Patentes_grouped_by_immatriculation[immatriculation] = []
            Patentes_grouped_by_immatriculation[immatriculation].append({
                'Patente': Patente,
                'vehicule_image_url': Patente.get_vehicule_image_url()
            })
        context['Patentes_grouped_by_immatriculation'] = Patentes_grouped_by_immatriculation
        return context



class PatenteCreateView(CreateView):
    model = Patente
    form_class = PatenteForm
    template_name = 'pages/Patente/create_Patente.html'
    success_url = reverse_lazy('list_Patente')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrer les choix de véhicules liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)

        form.fields['immatriculation'].queryset = proprietaire.vehicule_set.all()
        return form
   
    def get_form_valid_message(self):
        return "Nouvelle Patente ajoutée avec succès!"

    def form_valid(self, form):
        messages.success(self.request, "Ajout de la nouvelle Patente dans la base de données")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ERREUR !!! Une erreur s'est produite")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context


@method_decorator(login_required, name='dispatch')
class PatenteUpdateView(UpdateView):
    model = Patente
    form_class = PatenteForm
    template_name = "pages/Patente/create_Patente.html"
    success_url = reverse_lazy('list_Patente')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Patente, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context
    
    