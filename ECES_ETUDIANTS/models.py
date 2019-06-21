from django.db import models

#LE MODELE PERMET DE DEFINIR  NOS CLASS
# C'est ici que nous allons mettre toute nos classes
#de notre application
class Etudiant(models.Model):
	
	Nom=models.CharField(max_length=15)
	Prénom=models.CharField(max_length=15)
	Age=models.CharField(max_length=10)
	Adresse=models.CharField(max_length=30)
	Niveau=models.CharField(max_length=15)
	Option=models.CharField(max_length=25)
	Matricule=models.CharField(max_length=8,unique=True)
	Description=models.TextField()
	photos=models.FileField(upload_to="photo")
	
	def __str__ (self):
		return self.Nom.upper()

	class Meta:
 		ordering=('Matricule','Nom')
