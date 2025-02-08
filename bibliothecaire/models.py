from django.db import models

class Membre(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    optin = models.BooleanField(default=False)
    telephone = models.CharField(max_length=10, blank=True, null=True)
    date_inscription = models.DateField(auto_now_add=True)
