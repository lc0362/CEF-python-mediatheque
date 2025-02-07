from django.db import models

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=150)
    createur = models.CharField(max_length=150)
