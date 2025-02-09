from django.db import models
from .membre import Emprunteur

class Emprunt(models.Model):
    membre = models.ForeignKey("bibliothecaire.Emprunteur", related_name="emprunts", on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=[("livre", "Livre"), ("cd", "CD"), ("dvd", "DVD")])
    item_id = models.IntegerField()
    date_emprunt = models.DateField(auto_now_add=True)

    def give_back(self):
        """Retourne l'article emprunté"""
        self.delete()
        self.membre.check_bloque()  # Met à jour le statut du membre