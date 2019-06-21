from django.contrib import admin
from.models import Etudiant
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User,Group
# C'est  ici que l'on doit enregistrer tous nos modeles
#que nous avons défini dans le script model de notre application.
	
	


class EtudiantAdmin(admin.ModelAdmin):
	list_display=['Nom','Prénom','Age','Adresse','Niveau','Option','Matricule'
	,'Description','photos']
	list_display_links=('Nom','Prénom')
	search_fields=('Nom','Prénom','Matricule')
	fildsets=[ ("son nom",{'fields':["nom",]}),
			   ("son prenom",{'fields':["prenom",]}),
			   ("matricule",{'fields':["matricule",]})
	]




admin.site.register(Etudiant,EtudiantAdmin)
#admin.site.register(Etudiant)
admin.site.unregister(User)
admin.site.unregister(Group)
#pour changer le nom dun site au niveau de l'adminitration
#IL est obligatoire d'importé Adminite & User Group?
#et ne pas....



