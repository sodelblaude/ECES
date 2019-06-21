from django.urls import path
from.views import Profiles
from . import  views

urlpatterns = [
	path('', views.etudiant,name="acceuil"),
	path('acceuil/', views.acceuil,name="acceuil"),
	path('etudiant/', views.etudiant,name="etudiant"),
	path('profiles/<int:pk>',views.profiles,name="profiles"),
]
