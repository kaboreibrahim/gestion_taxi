"""
URL configuration for gestion_taxi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
 
from taxi.views.rapport import rapport_vehicule
from .views.Notebook import NotebookCreateView, load_chauffeurs,NotebookList,vehicule_list,vehicule_detail,change_statut_to_circulation,NotebookUpdateView
from .views.vidange import VidangeList,VidangeCreateView,VidangeUpdateView
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from taxi.views.index import index

from .views import afficher_informations_proprietaire,VehiculeList,VehiculeCreateView,\
    VehiculeUpdateView,afficher_details_vehicule,afficher_details_Vidange
    
from .views.liaison import LiaisonVehiculeChauffeurListView,LiaisonVehiculeChauffeurUpdateView\
    ,LiaisonVehiculeChauffeurCreateView
    
from .views.recette import RecetteDetails, RecetteList,RecetteUpdateView,RecetteCreateView

from .views.depense import DepenseList,DepenseUpdateView,DepenseCreateView,DepenseDetails

from .views.chauffeur import ChauffeurList,ChauffeurUpdateView,ChauffeurCreateView\
    ,afficher_details_Chauffeur
    
from .views.CarteStationnement import CarteStationnementList,CarteStationnementUpdateView,\
    CarteStationnementCreateView,afficher_details_CarteStationnement
    
from .views.Assurance import AssuranceList,AssuranceUpdateView,AssuranceCreateView,\
    AssuranceRappelView,afficher_details_Assurance,AssurancePdfView,send_email_reminders
    
from .views.Patente import PatenteList,PatenteCreateView,PatenteUpdateView,afficher_details_Patente

from .views.VisiteTechnique import VisiteTechniquePdfView,send_email_reminders_VT,\
    VisiteTechniqueList,VisiteTechniqueCreateView,VisiteTechniqueUpdateView,afficher_details_VisiteTechnique,VisiteTechniqueRappelView

from .views.Piece import PieceCreateView,PieceListView,afficher_details_Piece,PieceUpdateView

from .views.TypeDeVoiture import TypeDeVoitureCreateView,TypeDeVoitureListView,TypeDeVoitureUpdateView,afficher_details_TypeDeVoiture

from .views.ModeleDeVoiture import ModeleDeVoitureCreateView,ModeleDeVoitureListView,ModeleDeVoitureUpdateView,afficher_details_ModeleDeVoiture

from .views.EntreeStock import EntreeStockCreateView,EntreeStockListView,EntreeStockUpdateView,afficher_details_EntreeStock,get_stock_entre,StockPdfView

from .views.SortieStock import SortieStockCreateView,SortieStockListView,SortieStockUpdateView,afficher_details_SortieStock

from .views.auth import user_login,register,verify ,deconnection
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [

    path('index/',index,name="index"),

    # view proprietaire 
    
    path('proprietaire/info',afficher_informations_proprietaire,name='afficher_informations_proprietaire'),
    
    
    # view vehicule
    
    path('vehicule/list',VehiculeList.as_view(),name='list_voiture'),
    path('vehicule/create',VehiculeCreateView.as_view(),name='create_Vehicule'),
    path('vehicule/update/<uuid:pk>',VehiculeUpdateView.as_view(),name='updateview_Vehicule'),
    path('vehicule/detail/<uuid:detail_vehicule_id>',afficher_details_vehicule,name='Vehicule_detail'),
    
    # View  chauffeur 
    
    path('chauffuer/list',ChauffeurList.as_view(),name='list_Chauffeur'),
    path('chauffuer/update/<uuid:pk>',ChauffeurUpdateView.as_view(),name='update_Chauffeur'),
    path('chauffeur/create',ChauffeurCreateView.as_view(),name='create_Chauffeur'),
    path('chauffuer/detail/<uuid:detail_Chauffeur_id>',afficher_details_Chauffeur,name='details_Chauffeur'),
    
    #view laison vehicuel chauffeur 
    path ('liason/list',LiaisonVehiculeChauffeurListView.as_view(),name='liaison_list'),
    path ('liason/create',LiaisonVehiculeChauffeurCreateView.as_view(),name='liaison_create'),
    path ('liason/update/<uuid:pk>',LiaisonVehiculeChauffeurUpdateView.as_view(),name='updateview_liaison'),
    
    #view recette
    
    path('recette/list',RecetteList.as_view(),name='list_recette'),
    path('recette/create',RecetteCreateView.as_view(),name='create_recette'),
    path('recette/update/<uuid:pk>',RecetteUpdateView.as_view(),name='update_recette'),
    path('recette/details/', RecetteDetails.as_view(), name='recette_details'),    
    #view Depense
    
    path('Depense/list',DepenseList.as_view(),name='list_Depense'),
    path('Depense/create',DepenseCreateView.as_view(),name='create_Depense'),
    path('Depense/update/<uuid:pk>',DepenseUpdateView.as_view(),name='update_Depense'),
    path('Depnse/details/', DepenseDetails.as_view(), name='depense_details'),    

    # view vidange 
    
    path('Vidange/detail/<uuid:detail_Vidange_id>',afficher_details_Vidange,name='detail_Vidange'),
    path('Vidange/list',VidangeList.as_view(),name='list_Vidange'),
    path('Vidange/create',VidangeCreateView.as_view(),name='create_Vidange'),
    path('Vidange/update/<uuid:pk>',VidangeUpdateView.as_view(),name='update_Vidange'),
    
    
    #View Asssurance 
    
    path('Asssurance/detail/<uuid:detail_Assurance_id>',afficher_details_Assurance,name='detail_Assurance'),
    path('Asssurance/fin_du_mois',AssuranceRappelView.as_view(),name='assurances_proches_fin'),
    path('Asssurance/mail',send_email_reminders,name='send_email_reminders'),
    path('Asssurance/list',AssuranceList.as_view(),name='list_Assurance'),
    path('Asssurance/create',AssuranceCreateView.as_view(),name='create_Assurance'),
    path('Asssurance/update/<uuid:pk>',AssuranceUpdateView.as_view(),name='update_Assurance'),
    path('assurances_pdf/', AssurancePdfView.as_view(), name='assurance_pdf'),

    #view carte de staionnement

    path('CarteStationnement/detail/<uuid:detail_CarteStationnement_id>',afficher_details_CarteStationnement,name='detail_CarteStationnement'),
    path('CarteStationnement/list',CarteStationnementList.as_view(),name='list_CarteStationnement'),
    path('CarteStationnement/create',CarteStationnementCreateView.as_view(),name='create_CarteStationnement'),
    path('CarteStationnement/update/<uuid:pk>',CarteStationnementUpdateView.as_view(),name='update_CarteStationnement'),
    
    #view patente
    
    path('patente/detail/<uuid:detail_Patente_id>',afficher_details_Patente,name='detail_Patente'),
    path('Patente/list',PatenteList.as_view(),name='list_Patente'),
    path('Patente/create',PatenteCreateView.as_view(),name='create_Patente'),
    path('Patente/update/<uuid:pk>',PatenteUpdateView.as_view(),name='update_Patente'),
    
    #view visite technique 
    
    path('visite technique/detail/<uuid:detail_VisiteTechnique_id>',afficher_details_VisiteTechnique,name='detail_VisiteTechnique'),
    path('visite technique/list',VisiteTechniqueList.as_view(),name='list_VisiteTechnique'),
    path('visite technique/create',VisiteTechniqueCreateView.as_view(),name='create_VisiteTechnique'),
    path('visite technique/update/<uuid:pk>',VisiteTechniqueUpdateView.as_view(),name='update_VisiteTechnique'),
    path('visite technique/ fin ',VisiteTechniqueRappelView.as_view(),name='VisiteTechnique_proches_fin'),
    path('visite technique/ mail ',send_email_reminders_VT,name='send_email_reminders_VT'),
    path('visite technique_pdf/', VisiteTechniquePdfView.as_view(), name='VisiteTechniquePdfView'),
    
    # view piece
    
    path('piece/detail/<uuid:detail_Piece_id>',afficher_details_Piece,name='detail_Piece'),
    path('piece/list/',PieceListView.as_view(),name='Piece_list'),
    path('piece/create/',PieceCreateView.as_view(),name='Piece_create'),
    path('piece/update/<uuid:pk>',PieceUpdateView.as_view(),name='update_Piece'),
    
    #view typedevoiture
    
    
    path('Type/De/Voiture/detail/<uuid:detail_TypeDeVoiture_id>',afficher_details_TypeDeVoiture,name='detail_TypeDeVoiture'),
    path('TypeDeVoiture/list/',TypeDeVoitureListView.as_view(),name='TypeDeVoiture_list'),
    path('TypeDeVoiture/create/',TypeDeVoitureCreateView.as_view(),name='TypeDeVoiture_create'),
    path('TypeDeVoiture/update/<uuid:pk>',TypeDeVoitureUpdateView.as_view(),name='update_TypeDeVoiture'),
    
    #view modeledevoiture
      
    path('ModeleDeVoiture/detail/<uuid:detail_ModeleDeVoiture_id>',afficher_details_ModeleDeVoiture,name='detail_ModeleDeVoiture'),
    path('ModeleDeVoiture/list/',ModeleDeVoitureListView.as_view(),name='ModeleDeVoiture_list'),
    path('ModeleDeVoiture/create/',ModeleDeVoitureCreateView.as_view(),name='ModeleDeVoiture_create'),
    path('ModeleDeVoiture/update/<uuid:pk>',ModeleDeVoitureUpdateView.as_view(),name='update_ModeleDeVoiture'),
    
    # view entre de stock
    
    path('Entree/Stock/detail/<uuid:detail_EntreeStock_id>',afficher_details_EntreeStock,name='detail_EntreeStock'),
    path('Entree/Stock/list/',EntreeStockListView.as_view(),name='EntreeStock_list'),
    path('Entree/Stock/create/',EntreeStockCreateView.as_view(),name='EntreeStock_create'),
    path('Entree/Stock/update/<uuid:pk>',EntreeStockUpdateView.as_view(),name='update_EntreeStock'),
    path('Entree/Stock/get_stock',get_stock_entre,name='get_stock_entre'),
    path('generate_pdf/', StockPdfView.as_view(), name='StockPdfView'),
    # view entre de sortie
    
    path('Sortie/Stock/detail/<uuid:detail_SortieStock_id>',afficher_details_SortieStock,name='detail_SortieStock'),
    path('Sortie/Stock/list/',SortieStockListView.as_view(),name='SortieStock_list'),
    path('Sortie/Stock/create/',SortieStockCreateView.as_view(),name='SortieStock_create'),
    path('Sortie/Stock/update/<uuid:pk>',SortieStockUpdateView.as_view(),name='update_SortieStock'),
    
    #view  Notebook
    
    path('Notebook/list/',NotebookList.as_view(),name='Notebook_List'),

    path('vehicules/', vehicule_list, name='vehicule_list'),
    path('vehicule/notebook/detail/<uuid:vehicule_id>/', vehicule_detail, name='vehicule_detail'),
    path('notebook/<uuid:notebook_id>/change_statut/', change_statut_to_circulation, name='change_statut_to_circulation'),
    path('notebook/update/<uuid:pk>',NotebookUpdateView.as_view(),name='update_notebook'),
    path('Notebook/create',NotebookCreateView.as_view(),name='Create_Notebook'),
    #path('notebook/create',create_notebook,name='create_notebook'),
    path('ajax/load-chauffeurs/', load_chauffeurs, name='load_chauffeurs'),
    
    
    #view connextion 
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('deconnexion',deconnection,name='deconnexion'),
    path('verify/', verify, name='verify'),
    
     #view de recuperation de compte 
    path('reset-password/', PasswordResetView.as_view(template_name='pages/auth/password_reset.html'), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='pages/auth/password_reset_send.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='pages/auth/password_reset_form.html'), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='pages/auth/password_reset_done.html'), name='password_reset_complete'),
    
    path('rapport_vehicule/', rapport_vehicule, name='rapport_vehicule'),

   
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
