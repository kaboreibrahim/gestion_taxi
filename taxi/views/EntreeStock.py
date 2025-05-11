from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from taxi.forms import EntreeStockForm
from taxi.models import EntreeStock,Piece, Proprietaire,SortieStock
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from braces.views import FormMessagesMixin
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.db.models import Sum
from django.core.paginator import Paginator
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.colors import Color
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
import socket
from django.db.models import Q


@login_required
def get_stock_entre(request):
    
    # Get the logged-in user
    user = request.user

    # Get the Proprietaire instance associated with the logged-in user
    proprietaire = Proprietaire.objects.get(username=user.username)

    # Récupère toutes les pièces dans la base de données
    
    pieces = Piece.objects.filter(proprietaire=proprietaire)
    requete_recherche = request.GET.get('search')
    if requete_recherche:
        pieces = pieces.filter(Q(nom_piece__icontains=requete_recherche))

    # Pour chaque pièce, calcule les quantités restantes, sorties et reçues
    for piece in pieces:
        # Calcule la quantité totale reçue pour la pièce
        total_received = EntreeStock.objects.filter(piece=piece, proprietaire=proprietaire).aggregate(Sum("quantite"))["quantite__sum"] or 0

        # Calcule la quantité totale sortie pour la pièce
        total_sent = SortieStock.objects.filter(piece=piece, proprietaire=proprietaire).aggregate(Sum("quantite"))["quantite__sum"] or 0

        # Calcule la quantité restante pour la pièce
        remaining = total_received - total_sent

        # Ajoute les quantités calculées à la pièce
        piece.total_received = total_received
        piece.total_sent = total_sent
        piece.remaining = remaining
    
    # Retourne toutes les pièces avec les quantités calculées
    return render(request, "pages/EntreeStock/get_stock_entre.html", {'pieces': pieces})
class StockPdfView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
            
        proprietaire = Proprietaire.objects.get(username=user.username)
        pieces = Piece.objects.filter(proprietaire=proprietaire)


        # For each piece, calculate the remaining, received, and sent quantities
        for piece in pieces:
            total_received = EntreeStock.objects.filter(piece=piece, proprietaire=proprietaire).aggregate(Sum("quantite"))["quantite__sum"] or 0
            total_sent = SortieStock.objects.filter(piece=piece, proprietaire=proprietaire).aggregate(Sum("quantite"))["quantite__sum"] or 0
            remaining = total_received - total_sent

            # Add the calculated quantities to the piece
            piece.total_received = total_received
            piece.total_sent = total_sent
            piece.remaining = remaining

        # Create a new PDF file with ReportLab
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="stock_report.pdf"'

        # Create a PDF document object
        doc = SimpleDocTemplate(response, pagesize=letter)

        # Define data for the table
        data = [['Référence', 'Nom de la pièce', 'Modèle du véhicule', 'Quantité restante']]

        # Populate data from pieces
        for piece in pieces:
            data.append([str(piece.ref_piece), str(piece.nom_piece), str(piece.modele_de_voiture), str(piece.remaining)])

        light_blue = Color(0.88, 0.95, 1)  # Light blue shade
        dark_blue = Color(0.4, 0.65, 0.84)  # Dark blue shade

        # Create a table style
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), dark_blue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), light_blue),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        # Create a table object and apply style
        table = Table(data)
        table.setStyle(style)

        # Add table to the PDF document
        elements = []
        title = 'Rapport de stock'
        elements.append(Paragraph(title, getSampleStyleSheet()['Title']))
        elements.append(table)
        doc.build(elements)

        # Send the PDF as an email attachment
        subject = "Rapport de stock"
        email_to = "kaboremessi@gmail.com"  # Replace with the recipient's email address
        email_sent = self.send_pdf_as_email(subject, email_to, response.content)

        if email_sent:
            messages.success(request, "Un mail a été envoyé avec le rapport.")
        else:
            messages.error(request, "Problème de connexion, impossible d'envoyer le mail.")

        return response

    def send_pdf_as_email(self, subject, email_to, pdf_data, context=None):
        from_email = "kaboremessi@gmail.com"  # Replace with your sender email address

        # Generate the HTML content of the email from a template (optional)
        if context:
            html_content = render_to_string('email_template.html', context)
        else:
            html_content = None

        # Create the EmailMultiAlternatives object
        msg = EmailMultiAlternatives(subject, body="", from_email=from_email, to=[email_to])

        # Attach the PDF data
        msg.attach("stock_report.pdf", pdf_data, "application/pdf")

        # Add the HTML content if provided
        if html_content:
            msg.attach_alternative(html_content, "text/html")

        try:
            msg.send()
            return True
        except (socket.gaierror, Exception) as e:
            print(f"Erreur lors de l'envoi du courriel : {e}")
            return False

@method_decorator(login_required, name='dispatch')
class EntreeStockListView(ListView):
    """
        vue d'affichage de la liste des projects
    """
    model = EntreeStock
    context_object_name = 'EntreeStock_list'
    template_name = "pages/EntreeStock/list_EntreeStock.html"
    paginate_by = 10  # Définit le nombre d'éléments par page

    def get_queryset(self):
        
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        queryset = EntreeStock.objects.filter(proprietaire=proprietaire)
        queryset = queryset.order_by('-date_entree')

        return queryset
    
      
@method_decorator(login_required, name='dispatch')
class EntreeStockCreateView(FormMessagesMixin, CreateView):
    """
      Vue de création d'un EntreeStock
    """
    model = EntreeStock
    form_class = EntreeStockForm
    template_name = "pages/EntreeStock/EntreeStock_create.html"
    success_url = reverse_lazy('EntreeStock_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"
    form_valid_message = "L'entrée de stock a été ajoutée avec succès."

    def form_valid(self, form):
       
        piece = get_object_or_404(Piece, id=form.cleaned_data['piece'].id)
        quantite = form.cleaned_data['quantite']

        if quantite <= 0:
            messages.error(self.request, f'La quantité demandée ne peut pas être négative ou zéro')
            return super().form_invalid(form)
        
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        entrees = EntreeStock.objects.filter(piece=piece).aggregate(Sum("quantite"))["quantite__sum"] or 0
        total_entrees = entrees + quantite
        messages.info(self.request, f" vous avez ajouter {quantite}, {piece} \n . vous avez actuellement {total_entrees} ,{piece}  ")

        form.instance.proprietaire = proprietaire
        form.instance.piece = piece
        form.instance.quantite = quantite
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context


@method_decorator(login_required, name='dispatch')
class EntreeStockUpdateView(UpdateView):
    model = EntreeStock
    form_class = EntreeStockForm
    template_name = "pages/EntreeStock/EntreeStock_create.html"
    success_url = reverse_lazy('EntreeStock_list')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
       return "L'entrée de stock a été modifiée avec succès!"

    def form_valid(self, form):
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        piece = form.cleaned_data['piece']
        quantite = form.cleaned_data['quantite']

        if quantite <= 0:
            messages.error(self.request, f'La quantité demandée ne peut pas être négative ou zéro')
            return super().form_invalid(form)

        entrees = EntreeStock.objects.filter(piece=piece).exclude(id=self.object.id).aggregate(Sum("quantite"))["quantite__sum"] or 0
        total_entrees = entrees + quantite

        form.instance.Proprietaire =proprietaire
        form.instance.piece = piece
        form.instance.quantite = quantite

        messages.info(self.request, f"Vous avez modifié l'entrée de {quantite}, {piece}. Vous avez actuellement {total_entrees}, {piece} en stock.")

        return super().form_valid(form)
    
    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(EntreeStock, pk=pk)

    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # transmettez l'utilisateur connecté au formulaire
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context
    
    

def afficher_details_EntreeStock(request, detail_EntreeStock_id):
    detail_EntreeStock = get_object_or_404(EntreeStock, id=detail_EntreeStock_id)
    return render(request,"pages/EntreeStock/detail_EntreeStock.html", {'detail_EntreeStock': detail_EntreeStock})