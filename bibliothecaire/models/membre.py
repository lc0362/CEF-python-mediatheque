from django.db import models

class Emprunteur(models.Model):
    """Représente un membre-emprunteur avec une limite de 3 articles"""
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=10, null=True, blank=True)
    optin = models.BooleanField(default=False)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def nb_emprunts(self):
        """Compte le nombre d'emprunts actifs"""
        return self.emprunts.count()

    def check_bloque(self):
        """Met à jour le statut de blocage du membre"""
        self.bloque = self.nb_emprunts() >= 3
        self.save()

    def emprunter(self, item_type, item_id):
        """Ajoute un emprunt si possible"""
        print(f"Tentative d'emprunt de {item_type} (ID: {item_id}) par {self.prenom} {self.nom}")  # Debug
        if not self.bloque and self.nb_emprunts() < 3:
            from .emprunt import Emprunt  # Import interne pour éviter une boucle
            Emprunt.objects.create(membre=self, item_type=item_type, item_id=item_id)
            self.check_bloque()
            print(f"✔ {item_type} (ID: {item_id}) emprunté avec succès !")  # Debug
            return True
        print("⛔ Emprunt refusé : limite atteinte ou membre bloqué.")  # Debug
        return False

    def give_back(self, emprunt):
        """Supprime un emprunt et met à jour le statut de blocage"""
        print(f"🔄 Retour de {emprunt.item_type} (ID: {emprunt.item_id}) par {self.prenom} {self.nom}")  # Debug
        emprunt.delete()
        self.check_bloque()

