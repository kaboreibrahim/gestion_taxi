from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from taxi.forms import SortieStockForm
from taxi.models import SortieStock,Piece,EntreeStock,Proprietaire
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from braces.views import FormMessagesMixin
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.db.models import Sum
from django.core.paginator import Paginator

@method_decorator(login_required, name='dispatch')
class SortieStockListView(ListView):
    """
        vue d'affichage de la liste des projects
    """
    model = SortieStock
    context_object_name = 'SortieStock_list'
    template_name = "pages/SortieStock/list_SortieStock.html"
    paginate_by = 10  # Définit le nombre d'éléments par page

    def get_queryset(self):
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        queryset = SortieStock.objects.filter(proprietaire=proprietaire)
        queryset = queryset.order_by('-date_sortie')

        return queryset
    
      
    
@method_decorator(login_required, name='dispatch')
class SortieStockCreateView(FormMessagesMixin, CreateView):
    """
      Vue de création d'un SortieStock
    """
    model = SortieStock
    form_class = SortieStockForm
    template_name = "pages/SortieStock/SortieStock_create.html"
    success_url = reverse_lazy('SortieStock_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u" ajout de la nouvelle SortieStock avec succés!"
    def form_valid(self, form):
        
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username) 
        
        piece = get_object_or_404(Piece, id=form.cleaned_data['piece'].id)
        quantite = form.cleaned_data['quantite']
        vehicule = form.cleaned_data['vehicule']
        
        entrees = EntreeStock.objects.filter(piece=piece).aggregate(Sum("quantite"))["quantite__sum"] or 0
        sorties = SortieStock.objects.filter(piece=piece).aggregate(Sum("quantite"))["quantite__sum"] or 0
        
        stock_disponible = entrees - sorties
        print(stock_disponible)
        if quantite > stock_disponible:
            messages.error(self.request, f'La quantité restante de {piece} est de {stock_disponible} ')
            return super().form_invalid(form)
        
        if quantite <= 0:
            messages.error(self.request, f'La quantité demandée ne peut pas être négative ou zéro')
            return super().form_invalid(form)

       
        form.instance.proprietaire = proprietaire  # assignez le propriétaire connecté au nouveau véhicule
        form.instance.piece = piece
        form.instance.quantite = quantite
        form.instance.vehicule = vehicule
        if stock_disponible>=0:
            messages.info(self.request, f" vous avez retirer {quantite}, {piece}  pour envoyer a {vehicule}\n . vous avez actuellement {stock_disponible-quantite}  ,{piece} en stock ")
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # transmettez l'utilisateur connecté au formulaire
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context

@method_decorator(login_required, name='dispatch')
class SortieStockUpdateView(UpdateView):
    model = SortieStock
    form_class = SortieStockForm
    template_name = "pages/SortieStock/SortieStock_create.html"
    success_url = reverse_lazy('SortieStock_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return "La SortieStock a été modifiée avec succès!"
         
    
    def get_form_valid_message(self):
        return "La SortieStock a été modifiée avec succès!"

    def form_valid(self, form):
        piece = form.cleaned_data['piece']
        quantite = form.cleaned_data['quantite']
        vehicule = form.cleaned_data['vehicule']

        entrees = EntreeStock.objects.filter(piece=piece).aggregate(Sum("quantite"))["quantite__sum"] or 0
        sorties = SortieStock.objects.filter(piece=piece).exclude(id=self.object.id).aggregate(Sum("quantite"))["quantite__sum"] or 0

        stock_disponible = entrees - sorties

        if quantite <= 0:
            messages.error(self.request, f'La quantité demandée ne peut pas être négative ou zéro')
            return super().form_invalid(form)

        if quantite > stock_disponible:
            messages.error(self.request, f'La quantité demandée de {piece} est épuisée ')
            return super().form_invalid(form)

        form.instance.Proprietaire = self.request.user.proprietaire
        form.instance.piece = piece
        form.instance.quantite = quantite
        form.instance.vehicule = vehicule

        if stock_disponible >= 0:
            messages.info(self.request, f"Vous avez modifié la sortie de {quantite}, {piece} pour le véhicule {vehicule}. Vous avez actuellement {stock_disponible - quantite}, {piece} en stock.")

        return super().form_valid(form)


    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(SortieStock, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # transmettez l'utilisateur connecté au formulaire
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context
    

def afficher_details_SortieStock(request, detail_SortieStock_id):
    detail_SortieStock = get_object_or_404(SortieStock, id=detail_SortieStock_id)
    return render(request,"pages/SortieStock/detail_SortieStock.html", {'detail_SortieStock': detail_SortieStock})