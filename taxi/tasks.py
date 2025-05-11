from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Assurance, Vehicule, Proprietaire

@shared_task
def assurance_rappel_task():
    # Get all Proprietaire instances
    proprietaires = Proprietaire.objects.all()

    # Get the current date and time
    now = timezone.now()

    for proprietaire in proprietaires:
        # Filter vehicles linked to the current Proprietaire
        vehicules = Vehicule.objects.filter(Proprietaire=proprietaire)

        # Find all insurance policies that expire within the next three days
        queryset = Assurance.objects.filter(immatriculation__in=vehicules, Date_fin__range=(now + timedelta(days=1), now + timedelta(days=3))).order_by('Date_fin')

        # Send an email reminder for each insurance policy that expires soon
        for assurance in queryset:
            subject = f"Rappel : votre assurance {assurance.Label_assurance} expire bientôt"
            message = f"Bonjour,\n\nCeci est un rappel que votre assurance {assurance.Label_assurance} pour le véhicule {assurance.immatriculation} expire le {assurance.Date_fin}. Veuillez renouveler votre assurance avant cette date pour éviter toute interruption de couverture.\n\nCordialement,\nL'équipe d'assurance"
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[proprietaire.email],
                fail_silently=False,
            )
