from django.contrib import admin
from .models import  Proprietaire, Vehicule, Chauffeur, Vidange, VisiteTechnique,\
    Assurance, Patente, Recette, Depense, CarteStationnement,LiaisonVehiculeChauffeur,\
    Piece,EntreeStock,SortieStock,TypeDeVoiture,ModeleDeVoiture,Notebook,Fournisseurs
    
@admin.register(Piece)
class PieceAdmin(admin.ModelAdmin):
    list_display=('nom_piece','ref_piece','modele_de_voiture','Date_ajout','proprietaire','Nom_du_Founissuer')

@admin.register(EntreeStock)
class EntreeStockAdmin(admin.ModelAdmin):
    list_display=('quantite','piece','date_entree','proprietaire')    

@admin.register(SortieStock)
class SortieStockAdmin(admin.ModelAdmin):
    list_display=('quantite','piece','vehicule','date_sortie','proprietaire')    

@admin.register(TypeDeVoiture)
class TypeDeVoitureAdmin(admin.ModelAdmin):
    list_display=('nom','Proprietaire')
    
@admin.register(ModeleDeVoiture)
class ModelDeVoitureAdmin(admin.ModelAdmin):
    list_display=('nom','Proprietaire')


admin.site.register(LiaisonVehiculeChauffeur)
admin.site.register(Fournisseurs)


@admin.register(Proprietaire)
class ProprietaireAdmin(admin.ModelAdmin):
    list_display = ('username','N_CNI_proprietaire', 'N_registre_commerce','email','Contact')

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('Modele_voiture','Marque_voiture','immatriculation', 'Numero_chassis', 'Nbr_place', 'Couleur', 'Proprietaire')
    search_fields = ('Modele_voiture' ,'immatriculation')

@admin.register(Chauffeur)
class ChauffeurAdmin(admin.ModelAdmin):
    list_display = ( 'Nom', 'Prenom', 'N_permis', 'N_CNI_chauffeur', 'Annee_anciennete', 'Contact', 'Lieu_de_residence','proprietaire','Date_de_prise_service')
    search_fields = ('Nom', 'Prenom', 'N_permis')

@admin.register(Vidange)
class VidangeAdmin(admin.ModelAdmin):
    list_display = ( 'Nom_chauffeur', 'Date_vidange', 'Kilometrage_vidange', 'Kilometrage_prochaine_vidange', 'immatriculation')

@admin.register(VisiteTechnique)
class VisiteTechniqueAdmin(admin.ModelAdmin):
    list_display = (  'Date_de_debut', 'Date_de_fin', 'immatriculation', 'Centre_agree', 'Vignette', 'Numero_vignette','Montant','Observation')

@admin.register(Assurance)
class AssuranceAdmin(admin.ModelAdmin):
    list_display = ('Date_debut', 'Date_fin', 'immatriculation','Assureur','Montant_Assurance')

@admin.register(Patente)
class PatenteAdmin(admin.ModelAdmin):
    list_display = ( 'Label_patente', 'Date_debut', 'Date_fin', 'immatriculation')

@admin.register(Recette)
class RecetteAdmin(admin.ModelAdmin):
    list_display = ( 'Date_ajout', 'Montant', 'immatriculation')

@admin.register(Depense)
class DepenseAdmin(admin.ModelAdmin):
    list_display = ( 'piece', 'Montant','Nom_du_Founissuer','Date_ajout', 'Date_depense','immatriculation')

@admin.register(CarteStationnement)
class CarteStationnementAdmin(admin.ModelAdmin):
    list_display = ( 'Label_carte_stationnement', 'immatriculation', 'Date_de_debut', 'Date_de_fin')


@admin.register(Notebook)
class notebookAdmin(admin.ModelAdmin):
    list_display = ( 'date_arrivage', 'vehicule','statut_vehicule', 'motif','commentaire','date_sortie')
