from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=150)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey("bibliothecaire.Emprunteur", on_delete=models.SET_NULL, null=True, blank=True)

class Livre(Media):
    auteur = models.CharField(max_length=150)

class Dvd(Media):
    realisateur = models.CharField(max_length=150)

class Cd(Media):
    artiste = models.CharField(max_length=150)

