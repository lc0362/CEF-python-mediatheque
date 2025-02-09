"""from django.db import models
from mediatheque.models.media import Livre, Cd, Dvd  # Assurez-vous que les imports sont corrects

class Emprunteur(models.Model):
    name = models.CharField(max_length=255)
    bloque = models.BooleanField(default=False)
    emprunts = models.ManyToManyField(
        'mediatheque.Media',  # Lien générique aux médias
        blank=True,
        related_name="emprunteurs"
    )

    def __str__(self):
        return self.name

    def check_bloque(self):

        if self.emprunts.count() >= 3:
            self.bloque = True
        else:
            self.bloque = False
        self.save()

    def emprunter(self, media):

        if self.bloque:
            return False  # Refus d'emprunt car déjà bloqué
        if self.emprunts.count() < 3:
            self.emprunts.add(media)
            self.check_bloque()  # Vérifie après ajout
            return True
        return False

    def give_back(self, media):

        if media in self.emprunts.all():
            self.emprunts.remove(media)
            self.check_bloque()  # Vérifie après suppression
            return True
        return False
    """
