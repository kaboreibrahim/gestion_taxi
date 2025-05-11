from taxi.models import Proprietaire, VisiteTechnique,Vehicule
from taxi.forms import VisiteTechniqueForm
from django.views.generic import ListView,CreateView,UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy,reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import os
import requests
from django.views.generic import View
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import calendar
from django.core.paginator import Paginator
from django.db.models import Sum

def send_email_reminders_VT(request):
    # Get the logged-in user
    user = request.user

   
    proprietaire = Proprietaire.objects.get(username=user.username)

    # Filter vehicles linked to the logged-in user
    vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

    # Récupère la date et l'heure actuelles
    now = datetime.now()

    # Récupère le premier et le dernier jour du mois en cours
    first_day_of_month = now.replace(day=1)
    last_day_of_month = (now + timedelta(days=(32 if now.month in (1, 3, 5, 7, 8, 10, 12) else 31 if now.month in (4, 6, 9, 11) else 29))) - timedelta(days=1)
    last_day_of_month = last_day_of_month.replace(day=1)


    # Récupère toutes les visites techniques qui arrivent à échéance dans le mois en cours
    queryset = VisiteTechnique.objects.filter(immatriculation__in=vehicules, Date_de_fin__range=(first_day_of_month, last_day_of_month))
    print(f' la liste des visite technique qui fini dans le mois en cour :{queryset}')
    # Check if an internet connection is available
    try:
        requests.get('https://www.google.com', timeout=5)
    except requests.ConnectionError:
        messages.add_message(request, messages.ERROR, "Problème de connexion. Impossible d'envoyer les e-mails. Veuillez réessayer plus tard.")
        return redirect ('VisiteTechnique_proches_fin')


    # Send an email reminder for each insurance policy that expires soon
    for visiteTechnique in queryset:
        aujourdhui = timezone.now().date()
        days_between = (visiteTechnique.Date_de_fin - aujourdhui).days
        subject = f"Rappel : VisiteTechnique de vehicule {visiteTechnique.immatriculation} expire bientôt"
        message = f"Bonjour,\n\nNous vous rappelons que la visite technique  pour le véhicule immatriculé {visiteTechnique.immatriculation} , arrivera à échéance le {visiteTechnique.Date_de_fin}. La visite technique a une durée de {days_between} jours avant échéance.\n\n Afin d'éviter toute interruption de couverture, nous vous invitons à renouveler votre visiteTechnique avant cette date\n\nCordialement,\nL'équipe de visiteTechnique de gest-taxi"
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[proprietaire.email],
            fail_silently=False,
        )
    messages.add_message(request, messages.SUCCESS, "Le mail a été envoyé avec succès")
    return redirect ('VisiteTechnique_proches_fin')

class VisiteTechniquePdfView(View):
    def get(self, request, *args, **kwargs):
        # Get the logged-in user
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        # Filter vehicles linked to the logged-in user
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

        # Get the queryset of insurance policies that expire soon
       
        # Récupère la queryset des visites techniques qui se terminent bientôt
        today = datetime.now().date()

        # Récupère le premier et le dernier jour du mois en cours
        first_day_of_month = today.replace(day=1)
        last_day_of_month = (today + timedelta(days=(32 if today.month in (1, 3, 5, 7, 8, 10, 12) else 31 if today.month in (4, 6, 9, 11) else 29))) - timedelta(days=1)
        last_day_of_month = last_day_of_month.replace(day=1)

        #queryset = VisiteTechnique.objects.filter(immatriculation__in=vehicules, Date_de_fin__range=(first_day_of_month, last_day_of_month)).order_by('Date_de_fin')
        queryset = VisiteTechnique.objects.filter(immatriculation__in=vehicules,Date_de_fin__gte=today).order_by('Date_de_fin')


        # Get current month and year
        current_month = calendar.month_name[today.month]
        current_year = today.year

        # Convert month name to French
        month_names_fr = {
            'January': 'Janvier',
            'February': 'Février',
            'March': 'Mars',
            'April': 'Avril',
            'May': 'Mai',
            'June': 'Juin',
            'July': 'Juillet',
            'August': 'Août',
            'September': 'Septembre',
            'October': 'Octobre',
            'November': 'Novembre',
            'December': 'Décembre'
        }
        current_month_fr = month_names_fr.get(current_month, current_month)

        # Create a new PDF file with ReportLab
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="visite technique _{current_month_fr}_{current_year}.pdf"'

        # Create a PDF document object
        doc = SimpleDocTemplate(response, pagesize=letter)

        # Define data for the table
        data = [['N°', 'Immatriculation', 'Marque', 'Modèle','N° vignette','Jour de la semaine','Date', 'Semaine','Observation']]

        # Populate data from queryset
        for i, visiteTechnique in enumerate(queryset, start=1):
            date_fin = datetime.strptime(str(visiteTechnique.Date_de_fin), '%Y-%m-%d')
            day_of_week = date_fin.strftime('%A')
            day_of_week_fr = {
                'Monday': 'Lundi',
                'Tuesday': 'Mardi',
                'Wednesday': 'Mercredi',
                'Thursday': 'Jeudi',
                'Friday': 'Vendredi',
                'Saturday': 'Samedi',
                'Sunday': 'Dimanche',
            }.get(day_of_week, day_of_week)

            
            data.append([
                str(i),
                str(visiteTechnique.immatriculation.immatriculation),
                str(visiteTechnique.immatriculation.Marque_voiture),
                str(visiteTechnique.immatriculation.Modele_voiture),
                str(visiteTechnique.Numero_vignette),
                 day_of_week_fr,

                str(visiteTechnique.Date_de_fin.strftime('%d/%m/%Y')),
                str(visiteTechnique.semaine_du_mois()),  # Appel correct de la méthode
                str(visiteTechnique.Observation)
            ])

        # Create a table style
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.pink),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        # Create a table object and apply style
        table = Table(data)
        table.setStyle(style)

        # Add table to the PDF document
        elements = []
        title = f'VisiteTechnique du mois de {current_month_fr} {current_year}'
        elements.append(Paragraph(title, getSampleStyleSheet()['Title']))
        elements.append(table)
        doc.build(elements)

        return response
          

@method_decorator(login_required, name='dispatch')
class VisiteTechniqueRappelView(ListView):
    model = VisiteTechnique
    context_object_name = 'VisiteTechnique_proches_fin'
    template_name = 'pages/VisiteTechnique/VisiteTechnique_proches_fin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)# Assuming user has a OneToOneField to Proprietaire

         # Filter vehicles linked to the logged-in user
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)
        today = timezone.now().date()
        queryset = VisiteTechnique.objects.filter(immatriculation__in=vehicules,Date_de_fin__gte=today).order_by('Date_de_fin')
        
        
        # Calcul du montant total des assurances
        Montant_total = queryset.aggregate(total=Sum('Montant'))['total']
        print(queryset)
        context['total_montant']=Montant_total

        
        return context


    def get_queryset(self):
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)

        # Filter vehicles linked to the logged-in user
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)
        today = timezone.now().date()
        queryset = VisiteTechnique.objects.filter(immatriculation__in=vehicules,Date_de_fin__gte=today).order_by('Date_de_fin')

        
        # Apply filters
        marque = self.request.GET.get('marque')
        modele = self.request.GET.get('modele')
        centre_agree = self.request.GET.get('Centre_agree')
        semaine = self.request.GET.get('semaine')

        if marque:
            queryset = queryset.filter(immatriculation__Marque_voiture__id=marque)
        if modele:
            queryset = queryset.filter(immatriculation__Modele_voiture__id=modele)
        if centre_agree:
            queryset = queryset.filter(Centre_agree=centre_agree)
        if semaine:
            semaine = int(semaine)
            start_date = datetime(datetime.now().year, datetime.now().month, 1)
            end_date = start_date + timedelta(weeks=semaine)
            queryset = queryset.filter(Date_de_fin__gte=start_date, Date_de_fin__lt=end_date)
            


        return queryset

        

def afficher_details_VisiteTechnique(request, detail_VisiteTechnique_id):
    detail_VisiteTechnique = get_object_or_404(VisiteTechnique, id=detail_VisiteTechnique_id)
    return render(request,"pages/VisiteTechnique/detail_VisiteTechnique.html", {'detail_VisiteTechnique': detail_VisiteTechnique})

@method_decorator(login_required, name='dispatch')
class VisiteTechniqueList(ListView):
    model = VisiteTechnique
    context_object_name = 'list_VisiteTechnique'
    template_name = 'pages/VisiteTechnique/list_VisiteTechnique.html'
    #paginate_by = 10  # Définit le nombre d'éléments par page

    def get_queryset(self):

       # Récupérer l'utilisateur connecté
        user = self.request.user
        # Filtrer les véhicules liés au propriétaire connecté         
        proprietaire = Proprietaire.objects.get(username=user.username)
        # Filter vehicles linked to the logged-in user
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

        queryset = VisiteTechnique.objects.filter(immatriculation__in=vehicules)

        # Filtrer les VisiteTechniques en fonction des dates sélectionnées
        date_debut = self.request.GET.get('date_debut')
        date_fin = self.request.GET.get('date_fin')

        if date_debut and date_fin:
            date_fin = datetime.strptime(date_fin, '%Y-%m-%d') + timedelta(days=1)
            date_fin = date_fin.strftime('%Y-%m-%d')
            queryset = queryset.filter(Date_ajout__range=(date_debut, date_fin))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VisiteTechniques_grouped_by_immatriculation = {}
        for VisiteTechnique in context['list_VisiteTechnique']:
            immatriculation = VisiteTechnique.immatriculation
            if immatriculation not in VisiteTechniques_grouped_by_immatriculation:
                VisiteTechniques_grouped_by_immatriculation[immatriculation] = []
            VisiteTechniques_grouped_by_immatriculation[immatriculation].append({
                'VisiteTechnique': VisiteTechnique,
                'vehicule_image_url': VisiteTechnique.get_vehicule_image_url()
            })
        context['VisiteTechniques_grouped_by_immatriculation'] = VisiteTechniques_grouped_by_immatriculation
        return context

class VisiteTechniqueCreateView(CreateView):
    model = VisiteTechnique
    form_class = VisiteTechniqueForm
    template_name = 'pages/VisiteTechnique/create_VisiteTechnique.html'
    success_url = reverse_lazy('list_VisiteTechnique')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrer les choix de véhicules liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        form.fields['immatriculation'].queryset = proprietaire.vehicule_set.all()
        return form
   
    def get_form_valid_message(self):
        return "Nouvelle VisiteTechnique ajoutée avec succès!"

    def form_valid(self, form):
        messages.success(self.request, "Ajout de la nouvelle VisiteTechnique dans la base de données")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ERREUR !!! Une erreur s'est produite")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context


@method_decorator(login_required, name='dispatch')
class VisiteTechniqueUpdateView(UpdateView):
    model = VisiteTechnique
    form_class = VisiteTechniqueForm
    template_name = "pages/VisiteTechnique/create_VisiteTechnique.html"
    success_url = reverse_lazy('list_VisiteTechnique')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(VisiteTechnique, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context