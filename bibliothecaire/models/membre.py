from django.db import models
from django.utils.timezone import now
from datetime import timedelta

class Emprunteur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=10, null=True, blank=True)
    optin = models.BooleanField(default=False)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def nb_emprunts(self):
        return self.emprunts.count()

    def retards(self):
        une_semaine = now().date() - timedelta(days=7)
        return self.emprunts.filter(date_emprunt__lt=une_semaine).exists()

    def check_bloque(self):
        if self.nb_emprunts() >= 3 or self.retards():
            self.bloque = True
        else:
            self.bloque = False
        self.save()

    def emprunter(self, item_type, item_id):
        if not self.bloque and self.nb_emprunts() < 3:
            from .emprunt import Emprunt  # Import interne pour éviter une boucle
            Emprunt.objects.create(membre=self, item_type=item_type, item_id=item_id)
            self.check_bloque()
            return True
        return False

    def give_back(self, emprunt):
        emprunt.delete()
        self.check_bloque()

    def jours_depuis_ancien_emprunt(self):
        ancien_emprunt = self.emprunts.order_by("date_emprunt").first()
        if ancien_emprunt:
            return (now().date() - ancien_emprunt.date_emprunt).days
        return 0  # Aucun emprunt

