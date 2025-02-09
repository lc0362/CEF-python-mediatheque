"""from django.db import models
from mediatheque.models.membre import Emprunteur

    def nb_emprunts(self):
        return self.emprunt_set.count()

    def check_bloque(self):

        if self.nb_emprunts() >= 3:
            self.bloque = True
        else:
            self.bloque = False
        self.save()


class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=[('livre', 'Livre'), ('cd', 'CD'), ('dvd', 'DVD')])
    item_id = models.IntegerField()
    date_emprunt = models.DateField(auto_now_add=True)

    def give_back(self):
        self.delete()
        self.membre.check_bloque()
        """
