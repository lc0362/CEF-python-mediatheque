from django.db import models
from .membre import Emprunteur
from mediatheque.models.media import Livre, Cd, Dvd
import logging

logger = logging.getLogger(__name__)

class Emprunt(models.Model):
    membre = models.ForeignKey(Emprunteur, related_name="emprunts", on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=[("livre", "Livre"), ("cd", "CD"), ("dvd", "DVD")])
    item_id = models.IntegerField()
    date_emprunt = models.DateField(auto_now_add=True)

    def give_back(self):
        self.delete()
        self.membre.check_bloque()

    def get_item_name(self):
        item = None

        if self.item_type == "livre":
            item = Livre.objects.filter(id=self.item_id).first()
        elif self.item_type == "cd":
            item = Cd.objects.filter(id=self.item_id).first()
        elif self.item_type == "dvd":
            item = Dvd.objects.filter(id=self.item_id).first()

        if item:
            return item.name
        else:
            logger.warning(f"⚠️ Objet {self.item_type} avec id {self.item_id} introuvable !")
            return f"{self.item_type.capitalize()} inconnu (ID: {self.item_id})"