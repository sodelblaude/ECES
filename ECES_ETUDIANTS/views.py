from django.shortcuts import render
from .models import Etudiant
from django.views.generic import DetailView



def etudiant(request):
	etudiant=Etudiant.objects.all()
	return render(request,"pages/etudiant.html",{'etudiant':etudiant})

def acceuil(request):
	return render(request,"pages/acceuil.html")


def profiles(request,pk):
	vue=Etudiant.objects.get(pk=pk)
	return render(request,"pages/profiles.html",{'object':vue})


class Profiles(DetailView):
	model=Etudiant
	templates_name="pages/profiles.html"

	
	
# C'est ici que je dois mettre toute mes vue qui 
# va permettre de visueliser mon site sur le navigateur.
