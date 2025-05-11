from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from taxi.forms import PieceForm
from taxi.models import Piece, Proprietaire
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from braces.views import FormMessagesMixin
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.core.paginator import Paginator

@method_decorator(login_required, name='dispatch')
class PieceListView(ListView):
    """
        vue d'affichage de la liste des projects
    """
    model = Piece
    context_object_name = 'Piece_list'
    template_name = "pages/Piece/list_piece.html"
    paginate_by = 10  # Définit le nombre d'éléments par page1

    def get_queryset(self):
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)

        queryset = Piece.objects.filter(proprietaire=proprietaire)
        queryset = queryset.order_by('-Date_ajout')
        return queryset
    
      
    
@method_decorator(login_required, name='dispatch')
class PieceCreateView(FormMessagesMixin, CreateView):
    """
    Vue de création d'un Piece
    """
    model = Piece
    form_class = PieceForm
    template_name = "pages/Piece/Piece_create.html"
    success_url = reverse_lazy('Piece_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def form_valid(self, form):
        messages.success(self.request, "Liaison effectuée avec succès")
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrer les choix de véhicules liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        form.fields['modele_de_voiture'].queryset = proprietaire.modeledevoiture_set.all()

        return form

    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.FILES)
        form = PieceForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.instance.proprietaire = self.request.user  # Assigner directement l'utilisateur connecté
            form.save()
            return HttpResponseRedirect(reverse('Piece_list'))
        else:
            print(form.errors)
            messages.error(request, "ERREUR !!! Une erreur s'est produite")
            return HttpResponseRedirect(reverse('Piece_create'))

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
class PieceUpdateView(UpdateView):
    model = Piece
    form_class = PieceForm
    template_name = "pages/Piece/Piece_create.html"
    success_url = reverse_lazy('Piece_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Piece, pk=pk)

   
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['instance'] = self.object
        return kwargs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context
    

def afficher_details_Piece(request, detail_Piece_id):
    detail_Piece = get_object_or_404(Piece, id=detail_Piece_id)
    return render(request,"pages/Piece/detail_Piece.html", {'detail_Piece': detail_Piece})