from django.db import models
from django.contrib.auth.models import User
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
import uuid
from django_lifecycle import LifecycleModel
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os.path
from django.utils import timezone
from django.db.models import Sum
from django.core.exceptions import ValidationError
imageFs = FileSystemStorage(location=os.path.join(str(settings.BASE_DIR),
                                                 '/media/'))
from django.contrib.auth.models import AbstractUser
from datetime import timedelta


class Fournisseurs(SafeDeleteModel,LifecycleModel):
    
    _safedelete_policy=SOFT_DELETE_CASCADE
    id=models.UUIDField("ID",primary_key=True,default=uuid.uuid4,editable=False)
    Nom_Fournisseur = models.CharField(max_length=255)
    Telephone_Fournisseur=models.CharField( max_length=20)
    Localisation=models.CharField(max_length=50)
    Email_Fournisseur = models.CharField( max_length=50,blank=True,null=True,default="mail non spécifié" )
    
    
    def __str__(self):
        return f"{self.Nom_Fournisseur}  "
    
    

class Proprietaire(AbstractUser, SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    N_CNI_proprietaire = models.CharField(max_length=255)
    Proprietaire_CNI_photos = models.FileField("Document", upload_to='Proprietaire_CNI_documents/', blank=True, null=True)
    N_registre_commerce = models.CharField(max_length=255)
    Contact = models.CharField(max_length=20)
    Proprietaire_photos = models.ImageField("Photo", upload_to='Proprietaire_photos/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username  
class VerificationCode(models.Model):
    user = models.OneToOneField(Proprietaire, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.code}"
## la class des marques de voiture   
class TypeDeVoiture(SafeDeleteModel, LifecycleModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    Proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom}"
#class   des modeles de  voiture
class ModeleDeVoiture(SafeDeleteModel, LifecycleModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    Proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)

    def __str__(self):
        return f"   {self.nom}"
    
class Vehicule(SafeDeleteModel,LifecycleModel):
    
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4,
                          editable=False)
    Date_ajout = models.DateTimeField(default=timezone.now, editable=False)

    Date_mise_en_circulation = models.DateField()
    Marque_voiture = models.ForeignKey(TypeDeVoiture, on_delete=models.CASCADE,default='suzuki')
    Modele_voiture= models.ForeignKey(ModeleDeVoiture, on_delete=models.CASCADE)
    immatriculation = models.CharField(max_length=255, unique=True)
    Numero_chassis = models.CharField(max_length=255)
    Nbr_place = models.IntegerField()
    Couleur = models.CharField(max_length=255)
    vehicule_photos = models.ImageField("Photo", upload_to='Vehicule_photos/', blank=True, null=True)
    Proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    Label_voiture = models.IntegerField(default=0)
    
    # Champ pour le numéro de taxi
    
    def save(self, *args, **kwargs):
        if self.Label_voiture == 0:
            last_vehicule = Vehicule.objects.order_by('-Label_voiture').first()
            self.Label_voiture = last_vehicule.Label_voiture + 1 if last_vehicule else 1
        super(Vehicule, self).save(*args, **kwargs)
         
    def get_vehicule_photos_url(self):
        if self.vehicule_photos:
            return self.vehicule_photos.url
        else:
            return None

    def __str__(self):
        return f"  {self.immatriculation}"
    
class Chauffeur(SafeDeleteModel,LifecycleModel):
    
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4,
                          editable=False)
    
    Nom = models.CharField(max_length=255)
    Prenom = models.CharField(max_length=255) 
    N_permis = models.CharField(max_length=255)
    N_CNI_chauffeur = models.CharField(max_length=255)
    Chauffeur_CNI_photos = models.FileField("Document", upload_to='Chauffeur_CNI_photos/', blank=True, null=True)
    Annee_anciennete = models.CharField(max_length=255)
    Contact = models.CharField(max_length=20)
    Lieu_de_residence = models.CharField(max_length=255)
    Chauffeur_photos = models.ImageField("Photo", upload_to='Chauffeur_photos/', blank=True, null=True)
    Date_de_prise_service= models.DateField()
    Date_ajout = models.DateTimeField(default=timezone.now, editable=False)

    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, related_name='chauffeurs')

    def __str__(self):
        return f"{self.Nom} {self.Prenom} "

class LiaisonVehiculeChauffeur(models.Model):
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, related_name='liaison')
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE)
    Date_ajout = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f" {self.chauffeur}"
    
class Vidange(SafeDeleteModel,LifecycleModel):

    FILTRE_CHOICES = [
        ('oui', 'Oui'),
        ('non', 'Non'),
    ]
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4,
                          editable=False)

    Label_vidange = models.IntegerField(default=0)

    Filtre_a_huile = models.CharField(max_length=3, choices=FILTRE_CHOICES)
    Filtre_a_air = models.CharField(max_length=3, choices=FILTRE_CHOICES)
    Filtre_a_pollen = models.CharField(max_length=3, choices=FILTRE_CHOICES)
    Filtre_a_gasoil = models.CharField(max_length=3, choices=FILTRE_CHOICES)
    Kilometrage_vidange = models.IntegerField()
    Kilometrage_prochaine_vidange = models.IntegerField()
    Nom_chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE)
    Date_vidange = models.DateTimeField(default=timezone.now, editable=False)

    Observation = models.TextField()
    immatriculation = models.ForeignKey(Vehicule, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.Label_vidange == 0:
            last_vidange = Vidange.objects.filter(immatriculation=self.immatriculation).order_by('-Label_vidange').first()
            self.Label_vidange = last_vidange.Label_vidange + 1 if last_vidange else 1
        super(Vidange, self).save(*args, **kwargs)
        
    

    def get_vehicule_image_url(self):
        return self.immatriculation.get_vehicule_photos_url()

    def __str__(self):
        return f"Vidange - {self.Nom_chauffeur} - {self.Date_vidange} - kilo_vidange{self.Kilometrage_vidange}Km-  kilo-prochaine_vidange{self.Kilometrage_prochaine_vidange}Km"

class VisiteTechnique(SafeDeleteModel, LifecycleModel):
    """Model for tracking vehicle technical inspection visits."""

    CENTRE_AGREE_CHOICES = [
        ('SICTA', 'SICTA'),
        ('MAYELIA', 'MAYELIA'),
    ]
    
    VIGNETTE_CHOICES = [
        ('OUI', 'Vignette renouvelée'),
        ('NON', 'Vignette non renouvelée'),
    ]

    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    Ref = models.IntegerField(default=0)
    Date_de_debut = models.DateField()
    Date_de_fin = models.DateField()
    immatriculation = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    Centre_agree = models.CharField(max_length=8, default='SICTA', choices=CENTRE_AGREE_CHOICES)
    Vignette = models.CharField(max_length=3, default='OUI', choices=VIGNETTE_CHOICES)
    Numero_vignette = models.CharField(max_length=20, blank=True, null=True)  # Nouveau champ
    Montant = models.IntegerField()
    Observation = models.CharField(max_length=255, blank=True, null=True)  # Nouveau champ

    Date_ajout = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        indexes = [
            models.Index(fields=['Date_de_debut']),
            models.Index(fields=['Date_de_fin']),
            models.Index(fields=['immatriculation']),
        ]

    def save(self, *args, **kwargs):

        # Set the observation based on the Vignette status
        if self.Vignette == 'OUI':
            self.Observation = "VGNR"
        else:
            self.Observation = "VGR"

        super(VisiteTechnique, self).save(*args, **kwargs)
        
    def semaine_du_mois(self):
        # Obtenir le premier jour du mois de la Date_fin
        first_day_of_month = self.Date_de_fin.replace(day=1)
        # Calculer le nombre de semaines depuis le premier jour du mois
        delta_days = (self.Date_de_fin - first_day_of_month).days
        semaine = (delta_days // 7) + 1
        return semaine
    
    def jours_restants(self):
        # Calculer le nombre de jours restants avant la fin de la visite technique
        today = timezone.now().date()
        delta = self.Date_de_fin - today
        return delta.days
        
    

    def get_vehicule_image_url(self):
        """Returns the URL for the vehicle's image."""
        return self.immatriculation.get_vehicule_photos_url()

    def __str__(self):
        """String representation of the model instance."""
        return f"Visite Technique - {self.Ref} - {self.immatriculation}"
class Assurance(SafeDeleteModel,LifecycleModel):

    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4,
                          editable=False)

    ASSURANCE_CHOICES = [
        ('MATCA', 'MATCA'),
        ('ASACI', 'ASACI'),
    ]
    Label_assurance = models.IntegerField(default=0)
    immatriculation = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    Date_ajout = models.DateTimeField(default=timezone.now, editable=False)
    Date_debut = models.DateField()
    Date_fin = models.DateField()
    Assureur = models.CharField(max_length=255, choices=ASSURANCE_CHOICES,default="Assureur inconnu")
    Montant_Assurance =models.IntegerField()

    def save(self, *args, **kwargs):
        if self.Label_assurance == 0:
            last_assurance = Assurance.objects.filter(immatriculation=self.immatriculation).order_by('-Label_assurance').first()
            self.Label_assurance = last_assurance.Label_assurance + 1 if last_assurance else 1
        super(Assurance, self).save(*args, **kwargs)

    def get_vehicule_image_url(self):
        return self.immatriculation.get_vehicule_photos_url()
    
    def semaine_du_mois(self):
        # Obtenir le premier jour du mois de la Date_fin
        first_day_of_month = self.Date_fin.replace(day=1)
        # Calculer le nombre de semaines depuis le premier jour du mois
        delta_days = (self.Date_fin - first_day_of_month).days
        semaine = (delta_days // 7) + 1
        return semaine
    

    

    def __str__(self):
        return f" {self.immatriculation}"


class Patente(SafeDeleteModel,LifecycleModel):

    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4,
                          editable=False)

    Label_patente = models.IntegerField(default=0)
    Date_debut = models.DateField()
    Date_fin = models.DateField()
    immatriculation = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    Date_ajout = models.DateTimeField(default=timezone.now, editable=False)
    def save(self, *args, **kwargs):
        if self.Label_patente == 0:
            last_patente = Patente.objects.filter(immatriculation=self.immatriculation).order_by('-Label_patente').first()
            self.Label_patente = last_patente.Label_patente + 1 if last_patente else 1
        super(Patente, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.Label_patente} - {self.immatriculation}"

    def get_vehicule_image_url(self):
        return self.immatriculation.get_vehicule_photos_url()

class Piece(SafeDeleteModel, LifecycleModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    nom_piece = models.CharField(max_length=255)
    ref_piece=models.CharField(max_length=255)
    Nom_du_Founissuer=models.ForeignKey(Fournisseurs, on_delete=models.CASCADE)
    modele_de_voiture = models.ForeignKey(ModeleDeVoiture, on_delete=models.CASCADE)
    Date_ajout = models.DateTimeField(default=timezone.now, editable=False)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE,default='Inconnu')

    def __str__(self):
        return f"{self.nom_piece} {self.modele_de_voiture} "
    
class Recette(SafeDeleteModel,LifecycleModel):
    
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4,
                        editable=False)
    
    Date_ajout = models.DateTimeField(default=timezone.now, editable=False)
    immatriculation = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    Montant =  models.IntegerField()

    def get_vehicule_image_url(self):
            return self.immatriculation.get_vehicule_photos_url()

    def __str__(self):
        return f"Recette - {self.Montant} CFA - {self.immatriculation}"

class Depense(SafeDeleteModel,LifecycleModel):
    
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4,
                        editable=False)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    Montant =  models.IntegerField()
    Date_ajout = models.DateTimeField(default=timezone.now, editable=False)
    Date_depense= models.DateField()
    Nom_du_Founissuer=models.ForeignKey(Fournisseurs, on_delete=models.CASCADE)

    immatriculation = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    
    def get_vehicule_image_url(self):
        return self.immatriculation.get_vehicule_photos_url()

    def __str__(self):
        return f"{self.piece}- {self.Montant}CFA - {self.immatriculation}"
    
class CarteStationnement(SafeDeleteModel,LifecycleModel):

    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4,
                        editable=False)

    Date_de_debut = models.DateField()
    Date_de_fin = models.DateField()
    Label_carte_stationnement = models.IntegerField(default=0)
    immatriculation = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    Date_ajout = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if self.Label_carte_stationnement == 0:
            last_carte = CarteStationnement.objects.filter(immatriculation=self.immatriculation).order_by('-Label_carte_stationnement').first()
            self.Label_carte_stationnement = last_carte.Label_carte_stationnement + 1 if last_carte else 1
        super(CarteStationnement, self).save(*args, **kwargs)

    def get_vehicule_image_url(self):
            return self.immatriculation.get_vehicule_photos_url()

    def __str__(self):
        return f"{self.Label_carte_stationnement} - {self.immatriculation}"


    
class EntreeStock(SafeDeleteModel, LifecycleModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    date_entree = models.DateTimeField(default=timezone.now, editable=False)
    quantite = models.IntegerField()
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE,default='Inconnu')

    def __str__(self):
        return f"Entrée de {self.quantite} {self.piece} le {self.date_entree}"
    
    def clean_int(self):
      
        quantite = self.quantite

        piece=self.piece
        print(piece)
        line_int=EntreeStock.objects.filter(piece=piece)
        print(line_int)
        
        sum_line_int=line_int.aggregate(models.Sum("quantite"))["quantite__sum"] or 0
        k=sum_line_int+quantite
        
        
        if self.quantite<=0:
            raise ValidationError("La quantité demandée ne peut pas être négative ou zéro.")

            
        print(f"La somme des entrées : {k}")
    def save(self, *args, **kwargs):
        self.clean_int()
        super().save(*args, **kwargs)
  
        
        

class SortieStock(SafeDeleteModel, LifecycleModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    date_sortie = models.DateTimeField(default=timezone.now, editable=False)
    quantite = models.IntegerField()
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, blank=True, null=True)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE,default='Inconnu')

    def clean_out(self):
      
      
        piece = self.piece
        quantite = self.quantite
        print(self.piece)
        entrees = EntreeStock.objects.filter(piece=piece).aggregate(models.Sum("quantite"))["quantite__sum"] or 0
        print(f"La somme des entrées : {entrees}")
        sorties = SortieStock.objects.filter(piece=piece).aggregate(models.Sum("quantite"))["quantite__sum"] or 0
        print(f"La somme des sorties : {sorties}")


        stock_disponible = entrees - sorties
        k=stock_disponible-quantite
        print(f"La somme disponible : {k}")
        print(f"La quantité demandé : {quantite}")


        if self.quantite > stock_disponible:
            raise ValidationError("La quantité demandée est supérieure à la quantité disponible.")
        
    def save(self, *args, **kwargs):
        self.clean_out()
        super().save(*args, **kwargs)
  
        
    def __str__(self):
        return f"Sortie de {self.quantite} {self.piece} le {self.date_sortie} pour le vehicule {self.vehicule}"



class Notebook(SafeDeleteModel, LifecycleModel):
    
    RAISON_CHOICES = [
        ('En_panne', 'En panne'),
        ('visite_technique', 'Visite technique'),
    ]

    STATUT_CHOICES = [
        ('garage', 'Garage'),
        ('circulation', 'Circulation'),
    ]

    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    date_arrivage = models.DateTimeField(default=timezone.now, editable=False)
    vehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE, blank=True, null=True)
    statut_vehicule = models.CharField(max_length=15, default='garage', choices=STATUT_CHOICES, editable=False)
    motif = models.CharField(max_length=50, choices=RAISON_CHOICES)
    piece = models.ManyToManyField(Piece, blank=True, default=" aucune piece changer")
    commentaire = models.TextField()
    chauffeur=models.ForeignKey('LiaisonVehiculeChauffeur', on_delete=models.CASCADE, blank=True, null=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    
    Kilometrage = models.IntegerField()

   

    def change_statut_to_circulation(self):
        if self.statut_vehicule != 'circulation':
            self.statut_vehicule = 'circulation'
            self.date_sortie = timezone.now()
            self.save()

    def temps_passe_au_garage(self):
        if self.date_sortie:
            duration = self.date_arrivage - self.date_sortie 
        else:
            duration = timezone.now() - self.date_arrivage

        days = duration.days
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        return f"{days}j {hours}h {minutes}m"
    
    def save(self, *args, **kwargs):
        if self.pk is None:  # Check if this is a new record
            existing_notebook = Notebook.objects.filter(vehicule=self.vehicule, statut_vehicule='garage').first()
            if existing_notebook:
                raise ValidationError("Un enregistrement existe déjà pour ce véhicule avec le statut 'garage'.")
        super().save(*args, **kwargs)
    