from django.db import models

class Emprunteur(models.Model):
    name = models.CharField(max_length=255)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name
