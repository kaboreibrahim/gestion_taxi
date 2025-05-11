from django import forms

from .models import Vehicule,Chauffeur,LiaisonVehiculeChauffeur,Recette,Depense,\
    Vidange,Assurance, Patente,VisiteTechnique,CarteStationnement,Piece,SortieStock,\
    EntreeStock,TypeDeVoiture,ModeleDeVoiture,Proprietaire,Notebook,VerificationCode
from django.forms import  DateTimeInput

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.core.mail import send_mail
import random
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column
       
class VehiculeForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # get the logged-in user
        super().__init__(*args, **kwargs)
        """
        if self.user.is_authenticated:
            self.fields['Modele_voiture'].queryset = ModeleDeVoiture.objects.filter(Proprietaire=self.user.proprietaire)  # filter the modele_de_voiture field based on the logged-in owner
 """
    class Meta:
        model = Vehicule
        fields = ['Marque_voiture','Modele_voiture','immatriculation','Numero_chassis','Nbr_place','Date_mise_en_circulation','Couleur','vehicule_photos']
        widgets={
            'Date_mise_en_circulation':DateTimeInput(attrs={"type": "date"}),
            'Annee_fabrication':DateTimeInput(attrs={"type": "date"}),
        }
       



class ChauffeurForm (forms.ModelForm):
    
    
    def __init__(self, *args,**kwargs):
        
        super(ChauffeurForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.layout=Layout(
            Column(
                'Nom',
                'Prenom',
                'N_permis',
                'N_CNI_chauffeur',
                'Chauffeur_CNI_photos',
                'Annee_anciennete',
                'Contact',
                'Lieu_de_residence',
                'Date_de_prise_service',
                'Chauffeur_photos',  
               
            )
        )
        
    class Meta:
        model=Chauffeur
        fields = ['Nom','Prenom','N_permis','N_CNI_chauffeur','Chauffeur_CNI_photos','Annee_anciennete','Contact','Lieu_de_residence','Date_de_prise_service', 'Chauffeur_photos']
        widgets={
            'Date_de_prise_service':DateTimeInput(attrs={"type": "date"}),
        }
        labels = {
            'N_permis': 'N° de permis ',
            'Chauffeur_photos': 'Ajouter la  photo du chauffeur',
            'N_CNI_chauffeur': 'N° de CNI du chauffeur',
            'Chauffeur_CNI_photos': 'Ajouter la CNI du chauffuer (PDF)',
        }
class LiaisonVehiculeChauffeurForm(forms.ModelForm):
    class Meta:
        model = LiaisonVehiculeChauffeur
        fields = ['vehicule','chauffeur']
        
    
        
class recetteForm(forms.ModelForm):
   
    class Meta:
        model = Recette
        fields = ['immatriculation','Montant']
       

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = '__all__'
        widgets={
                'Date_depense':DateTimeInput(attrs={"type": "date"}),
            }
        

class VidangeForm(forms.ModelForm):
    
    
    class Meta:
        model=Vidange
        fields=['immatriculation','Filtre_a_huile','Filtre_a_air','Filtre_a_pollen','Filtre_a_gasoil','Kilometrage_vidange','Kilometrage_prochaine_vidange','Nom_chauffeur','Observation']
        labels = {
            'immatriculation': ' Vehicule',
          
        }
    
        
class AssuaranceForm(forms.ModelForm):
    
    class Meta:
        model=Assurance
        fields=['immatriculation','Assureur','Montant_Assurance','Date_debut','Date_fin',]
        widgets={
                    'Date_debut':DateTimeInput(attrs={"type": "date"}),
                    'Date_fin':DateTimeInput(attrs={"type": "date"}),
                }
            
class PatenteForm(forms.ModelForm):
    
    class Meta:
        model=Patente
        fields=['immatriculation','Date_debut','Date_fin',]

        widgets={
                    'Date_debut':DateTimeInput(attrs={"type": "date"}),
                    'Date_fin':DateTimeInput(attrs={"type": "date"}),
                }
        
class VisiteTechniqueForm(forms.ModelForm):
    
    class Meta:
        model=VisiteTechnique
        fields = ['Date_de_debut', 'Date_de_fin', 'immatriculation', 'Centre_agree', 'Vignette', 'Numero_vignette','Montant']

        widgets={
                    'Date_de_debut':DateTimeInput(attrs={"type": "date"}),
                    'Date_de_fin':DateTimeInput(attrs={"type": "date"}),
                }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Numero_vignette'].required = False  # Rend le champ optionnel
        self.fields['Numero_vignette'].widget.attrs.update({'class': 'hidden'})  # Cache le champ initialement
        
class CarteStationnementForm(forms.ModelForm):
    
    class Meta:
        model=CarteStationnement
        fields=['immatriculation','Date_de_debut','Date_de_fin']
        widgets={
                    'Date_de_debut':DateTimeInput(attrs={"type": "date"}),
                    'Date_de_fin':DateTimeInput(attrs={"type": "date"}),
                }

class PieceForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # get the logged-in user
        super().__init__(*args, **kwargs)
    
    """    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # get the logged-in user
        super().__init__(*args, **kwargs)
        if self.user.is_authenticated:
            self.fields['modele_de_voiture'].queryset = ModeleDeVoiture.objects.filter(Proprietaire=self.user.proprietaire)  # filter the modele_de_voiture field based on the logged-in owner
    
  
"""
        
    class Meta:
        model=Piece
        fields=['nom_piece','Nom_du_Founissuer','ref_piece','modele_de_voiture']
        labels = {
            'modele_de_voiture': ' modele de voiture',
            'ref_piece':'reference de la piece'
        }

class TypeDeVoitureForm (forms.ModelForm):
    
    def __init__(self, *args,**kwargs):
        
        super(TypeDeVoitureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.layout=Layout(
            Column(
                'nom',
                
            )
        )
    
    class Meta:
        model=TypeDeVoiture
        fields=['nom']
        labels = {
            'nom': 'Marque du vehicule ',
        }

class ModeleDeVoitureForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # get the logged-in user
        super().__init__(*args, **kwargs)
        
    
    class Meta:
        model= ModeleDeVoiture
        fields=['nom']
        labels = {
            'nom': 'Modele',
        }


class EntreeStockForm(forms.ModelForm):
   
  
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # get the logged-in user
        super().__init__(*args, **kwargs)
        if self.user.is_authenticated:
            
            user = self.user
            proprietaire = Proprietaire.objects.get(username=user.username)
            self.fields['piece'].queryset = Piece.objects.filter(proprietaire=proprietaire)  # filter the modele_de_voiture field based on the logged-in owner


    class Meta:
        model= EntreeStock
        fields=['piece','quantite']
      
class SortieStockForm(forms.ModelForm):
   
    
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # get the logged-in user
        super().__init__(*args, **kwargs)
        if self.user.is_authenticated:
            user = self.user
            proprietaire = Proprietaire.objects.get(username=user.username)
            self.fields['piece'].queryset = Piece.objects.filter(proprietaire=proprietaire)  # filter the modele_de_voiture field based on the logged-in owner
            self.fields['vehicule'].queryset = Vehicule.objects.filter(Proprietaire=proprietaire)  # filter the modele_de_voiture field based on the logged-in owner


    class Meta:
        model= SortieStock
        fields=['piece','quantite','vehicule']
      
class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ['vehicule',  'motif', 'piece','Kilometrage', 'commentaire', 'chauffeur']
        
    def clean(self):
        cleaned_data = super().clean()
        vehicule = cleaned_data.get('vehicule')

        if vehicule:
            existing_notebook = Notebook.objects.filter(vehicule=vehicule, statut_vehicule='garage').first()
            if existing_notebook:
                raise ValidationError("le  véhicule est déjà au  garage. ")

        return cleaned_data

    #vehicule = forms.ModelChoiceField(queryset=Vehicule.objects.all(), required=True)
    #chauffeur = forms.ModelChoiceField(queryset=Chauffeur.objects.none(), required=True)

    """ 
        def __init__(self, *args, **kwargs):
        super(NotebookForm, self).__init__(*args, **kwargs)
        if 'vehicule' in self.data:
            try:
                vehicule_id = int(self.data.get('vehicule'))
                self.fields['chauffeur'].queryset = Chauffeur.objects.filter(liaisonvehiculechauffeur__vehicule_id=vehicule_id).distinct()
            except (ValueError, TypeError):
                self.fields['chauffeur'].queryset = Chauffeur.objects.none()
        elif self.instance.pk:
            self.fields['chauffeur'].queryset = Chauffeur.objects.filter(liaisonvehiculechauffeur__vehicule_id=self.instance.vehicule_id).distinct()
        """
            

class  PropietaireForm(UserCreationForm):
    class Meta:
        model = Proprietaire
        fields = ('first_name','last_name','Proprietaire_photos', 'email','Contact','N_registre_commerce','username','N_CNI_proprietaire','Proprietaire_CNI_photos','password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Proprietaire.objects.filter(email=email).exists():
            raise ValidationError("Un compte avec cet e-mail existe déjà.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # Désactiver le compte jusqu'à la vérification
        if commit:
            user.save()
            code = str(random.randint(100000, 999999))
            VerificationCode.objects.create(user=user, code=code)
            send_mail(
                'Votre code de vérification',
                f'Votre code de vérification est {code}',
                'kaboremessi@gmail.com',
                [user.email],
                fail_silently=False,
            )
        return user
    

class LoginForm(AuthenticationForm): 
    
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur ou e-mail', 'id': 'username'})
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe', 'id': 'password'})
    )
    
class VerificationForm(forms.Form):
 
    code = forms.CharField(max_length=6)