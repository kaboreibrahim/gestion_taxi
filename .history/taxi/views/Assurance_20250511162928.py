from taxi.models import Assurance,Vehicule,TypeDeVoiture,ModeleDeVoiture,Proprietaire
from taxi.forms import AssuaranceForm
from django.views.generic import ListView,CreateView,UpdateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta,date
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import requests
from django.views.generic import View
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import calendar
from django.core.paginator import Paginator
from django.shortcuts import redirect
import locale

from django.views import View
from django.db.models import Sum


try:
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
except locale.Error:
    # Si la locale n'est pas disponible, on utilise la locale par défaut
    locale.setlocale(locale.LC_TIME, '')


def get_jours_feries():
    return [
        date(2024, 1, 1),  # Nouvel An
        date(2024, 3, 20),  # Équinoxe de mars
        date(2024, 4, 1),  # Lundi de Pâques
        date(2024, 4, 6),  # Laila tou-Kadr
        date(2024, 4, 10),  # Aïd al-Fitr
        date(2024, 5, 1),  # Fête du Travail
        date(2024, 5, 9),  # Ascension
        date(2024, 5, 18),  # test
        date(2024, 5, 20),  # Lundi de Pentecôte
        date(2024, 6, 17),  # Aïd al-Kébir
        date(2024, 8, 7),  # Jour de l'Indépendance
        date(2024, 8, 15),  # Assomption de Marie
        date(2024, 9, 16),  # Anniversaire du Prophète
        date(2024, 9, 22),  # Équinoxe de septembre
        date(2024, 11, 1),  # Toussaint
        date(2024, 11, 15),  # Journée Nationale de la Paix
        date(2024, 12, 21),  # Solstice de décembre
        date(2024, 12, 25)  # Noël
    ]

def send_email_reminders(request):
    user = request.user
    proprietaire = user.proprietaire
    vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)
    today = timezone.now().date()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    queryset = Assurance.objects.filter(immatriculation__in=vehicules, Date_fin__range=(today, week_end)).order_by('Date_fin')

    try:
        requests.get('https://www.google.com', timeout=5)
    except requests.ConnectionError:
        messages.add_message(request, messages.ERROR, "Problème de connexion. Impossible d'envoyer les e-mails. Veuillez réessayer plus tard.")
        return redirect('assurances_proches_fin')

    jours_feries = get_jours_feries()
    assurances_par_courriel = {}

    for assurance in queryset:
        proprietaire_courriel = proprietaire.Mail
        if proprietaire_courriel in assurances_par_courriel:
            assurances_par_courriel[proprietaire_courriel].append(assurance)
        else:
            assurances_par_courriel[proprietaire_courriel] = [assurance]

    for proprietaire_courriel, assurances in assurances_par_courriel.items():
        objet = "Rappel : l'assurance de plusieurs véhicules expire bientôt"
        message = "Bonjour,\n\nNous vous rappelons que les assurances des véhicules suivants arrivent à échéance dans la semaine à venir :  \n"

        for assurance in assurances:
            aujourdhui = timezone.now().date()
            jours_entre = (assurance.Date_fin - aujourdhui).days
            jour_semaine_fin = assurance.Date_fin.strftime('%A')
            if assurance.Date_fin in jours_feries:
                if assurance.Date_fin.weekday() == 0:  # Vérifier si c'est un lundi
                    rappel_avance = assurance.Date_fin - timedelta(days=7)  # Rappel une semaine avant
                    message += f"\n- Véhicule immatriculé {assurance.immatriculation}, arrivera à échéance le {jour_semaine_fin}  {assurance.Date_fin} (Jour férié lundi). Rappel envoyé pour {rappel_avance}."
                else:
                    message += f"\n- Véhicule immatriculé {assurance.immatriculation}, arrivera à échéance le {jour_semaine_fin} {assurance.Date_fin} (Jour férié). Il reste {jours_entre} jours avant échéance."
            else:
                message += f"\n- Véhicule immatriculé {assurance.immatriculation}, arrivera à échéance le {jour_semaine_fin} {assurance.Date_fin}. Il reste {jours_entre} jours avant échéance."

        message += "\n\nAfin d'éviter toute interruption de couverture, nous vous invitons à renouveler votre assurance avant ces dates.\n\nCordialement,\nL'équipe d'assurance de gest-taxi"

        send_mail(
            subject=objet,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            #recipient_list=[proprietaire_courriel,'ousmanekaborre@gmail.com','kamtransitaire@gmail.com'],
            recipient_list=[proprietaire_courriel],
            fail_silently=False,
        )

    messages.add_message(request, messages.SUCCESS, "Les courriels ont été envoyés avec succès")
    return redirect('assurances_proches_fin')

class AssurancePdfView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)

        # Filter vehicles linked to the logged-in user
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

        # Get the queryset of insurance policies that expire soon
        today = timezone.now().date()
        queryset = Assurance.objects.filter(immatriculation__in=vehicules, Date_fin__gte=today).order_by('Date_fin')
        
        # Calcul du montant total des assurances
        total_montant = queryset.aggregate(total=Sum('Montant_Assurance'))['total']
        
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
            'December': 'Décembre',
        }
        
        current_month_fr = month_names_fr.get(current_month, current_month)

        # Create a new PDF file with ReportLab
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="assurance_{current_month_fr}_{current_year}.pdf"'

        # Create a PDF document object
        doc = SimpleDocTemplate(response, pagesize=letter)

        # Define data for the table
        data = [['N°', 'Immatriculation', 'Marque', 'Modèle', 'Assureur', 'Mois', 'Date', 'Jour de la semaine', 'Semaine', 'Montant']]

        # Populate data from queryset
        for i, assurance in enumerate(queryset, start=1):
            date_fin = datetime.strptime(str(assurance.Date_fin), '%Y-%m-%d')
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
                str(assurance.immatriculation.immatriculation),
                str(assurance.immatriculation.Marque_voiture),
                str(assurance.immatriculation.Modele_voiture),
                str(assurance.Assureur),
                str(assurance.Date_fin.strftime("%B")),
                str(assurance.Date_fin.strftime('%d/%m/%Y')),
                day_of_week_fr,
                str(assurance.semaine_du_mois()),  # Appel correct de la méthode
                str(assurance.Montant_Assurance)
            ])

        # Ajouter une ligne pour le montant total
        data.append([
            '', '', '', '', '', '', '', '', 'TOTAL :', str(total_montant)
        ])

        # Create a table style
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('SPAN', (0, -1), (-3, -1)),  # Fusionne les premières cellules de la dernière ligne
            ('ALIGN', (0, -1), (-1, -1), 'CENTER'),  # Centre le contenu de la dernière cellule
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),  # Met en gras la dernière cellule
        ])

        # Create a table object and apply style
        table = Table(data)
        table.setStyle(style)

        # Add table to the PDF document
        elements = []
        title = f'Assurance du mois de {current_month_fr} {current_year}'
        elements.append(Paragraph(title, getSampleStyleSheet()['Title']))
        elements.append(table)
        doc.build(elements)

        return response


@method_decorator(login_required, name='dispatch')
class AssuranceRappelView(ListView):
    model = Assurance
    context_object_name = 'assurances_proches_fin'
    template_name = 'pages/Assurance/assurances_proches_fin.html'

    def get_queryset(self):
         # Filtrer les choix de véhicules liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)
        today = timezone.now().date()
        queryset = Assurance.objects.filter(
            immatriculation__in=vehicules,
            Date_fin__gte=today
        ).order_by('Date_fin')
        
         # Calcul du montant total des assurances
        total_montant = queryset.aggregate(total=Sum('Montant_Assurance'))['total']
        # Affichage du montant total
        print(f"Le montant total des assurances est : {total_montant}")

        # Apply filters
        marque = self.request.GET.get('marque')
        modele = self.request.GET.get('modele')
        assureur = self.request.GET.get('assureur')
        semaine = self.request.GET.get('semaine')

        if marque:
            queryset = queryset.filter(immatriculation__Marque_voiture__id=marque)
        if modele:
            queryset = queryset.filter(immatriculation__Modele_voiture__id=modele)
        if assureur:
            queryset = queryset.filter(Assureur=assureur)
        if semaine:
            semaine = int(semaine)
            start_date = datetime(datetime.now().year, datetime.now().month, 1)
            end_date = start_date + timedelta(weeks=semaine)
            queryset = queryset.filter(Date_fin__gte=start_date, Date_fin__lt=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        current_month = now.month
        current_year = now.year
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)
        today = timezone.now().date()
        queryset = Assurance.objects.filter(
            immatriculation__in=vehicules,
            Date_fin__gte=today
        ).order_by('Date_fin')
        
        # Calcul du montant total des assurances
        total_montant = queryset.aggregate(total=Sum('Montant_Assurance'))['total']
        # Affichage du montant total
        print(f"Le montant total des assurances est : {total_montant}")
        
        weeks = set()
        start_date = datetime(current_year, current_month, 1)
        for i in range(5):  # Max 5 weeks in a month
            end_date = start_date + timedelta(weeks=i)
            if end_date.month == current_month:
                weeks.add(i + 1)
            else:
                break

        context['semaines'] = sorted(list(weeks))
        context['marques'] = TypeDeVoiture.objects.all()
        context['modeles'] = ModeleDeVoiture.objects.all()
        context['assureurs'] = [choice[0] for choice in Assurance.ASSURANCE_CHOICES]
        context['total_montant']=total_montant
        return context


   
   
   
def afficher_details_Assurance(request, detail_Assurance_id):
    detail_Assurance = get_object_or_404(Assurance, id=detail_Assurance_id)
    return render(request,"pages/Assurance/detail_assusrance.html", {'detail_Assurance': detail_Assurance})

@method_decorator(login_required, name='dispatch')
class AssuranceList(ListView):
    model = Assurance
    context_object_name = 'list_Assurance'
    template_name = 'pages/Assurance/list_Assurance.html'

    def get_queryset(self):
       
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)

        # Filter vehicles linked to the logged-in user
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

        queryset = Assurance.objects.filter(immatriculation__in=vehicules)

        # Filtrer les assurances en fonction des dates sélectionnées
        date_debut = self.request.GET.get('date_debut')
        date_fin = self.request.GET.get('date_fin')

        if date_debut and date_fin:
            date_fin = datetime.strptime(date_fin, '%Y-%m-%d') + timedelta(days=1)
            date_fin = date_fin.strftime('%Y-%m-%d')
            queryset = queryset.filter(Date_ajout__range=(date_debut, date_fin))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assurances_grouped_by_immatriculation = {}
        for assurance in context['list_Assurance']:
            immatriculation = assurance.immatriculation
            if immatriculation not in assurances_grouped_by_immatriculation:
                assurances_grouped_by_immatriculation[immatriculation] = []
            assurances_grouped_by_immatriculation[immatriculation].append({
                'assurance': assurance,
                'vehicule_image_url': assurance.get_vehicule_image_url(),
            })
        context['assurances_grouped_by_immatriculation'] = assurances_grouped_by_immatriculation
        return context


class AssuranceCreateView(CreateView):
    model = Assurance
    form_class = AssuaranceForm
    template_name = 'pages/Assurance/create_Assurance.html'
    success_url = reverse_lazy('list_Assurance')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
         # Filtrer les choix de véhicules liés au propriétaire connecté
        user = self.request.user
        proprietaire = Proprietaire.objects.get(username=user.username)
        form.fields['immatriculation'].queryset = proprietaire.vehicule_set.all()
        return form
   
    def get_form_valid_message(self):
        return "Nouvelle assurance ajoutée avec succès!"

    def form_valid(self, form):
        messages.success(self.request, "Ajout de la nouvelle assurance dans la base de données")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ERREUR !!! Une erreur s'est produite")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "post"
        return context


@method_decorator(login_required, name='dispatch')
class AssuranceUpdateView(UpdateView):
    model = Assurance
    form_class = AssuaranceForm
    template_name = "pages/Assurance/create_Assurance.html"
    success_url = reverse_lazy('list_Assurance')
    form_invalid_message = "Oups, quelque chose s'est mal passé!"

    def get_form_valid_message(self):
        return u"Modification effectuée avec succès!"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Assurance, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Pass the instance to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = "put"
        return context
    
    
    
