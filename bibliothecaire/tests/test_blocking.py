from django.test import TestCase
from django.utils.timezone import now
from datetime import timedelta
from bibliothecaire.models.membre import Emprunteur
from bibliothecaire.models.emprunt import Emprunt
from mediatheque.models.media import Livre, Cd, Dvd
from django.contrib.auth.models import User

class TestBlockingSystem(TestCase):
    def setUp(self):
        """Création des données admin et membre pour les tests"""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.membre = Emprunteur.objects.create(
            nom="Does", prenom="Jonathan", email="john@example.com", telephone="0601010101"
        )
        self.livre = Livre.objects.create(name="Livre Test", auteur="Auteur Test")
        self.cd = Cd.objects.create(name="CD Test", artiste="Artiste Test")
        self.dvd = Dvd.objects.create(name="DVD Test", realisateur="Réalisateur Test")

    def test_check_bloque(self):
        """Test : Un membre est bloqué après un emprunt en retard"""
        # Création d'un emprunt en retard à 8 jours
        emprunt = Emprunt.objects.create(membre=self.membre, item_type="livre", item_id=self.livre.id)
        emprunt.date_emprunt = now().date() - timedelta(days=8)
        emprunt.save()

        # Vérification que le membre est bloqué
        self.membre.check_bloque()
        self.assertTrue(self.membre.bloque, "Le membre doit être bloqué après un emprunt en retard")

        # Suppression de l'emprunt (retour du livre)
        emprunt.give_back()

        # Rafraichi l'objet et vérifie le déblocage
        self.membre.refresh_from_db()
        self.assertFalse(self.membre.bloque, "Le membre devrait être débloqué après retour du livre")

    def test_4_items(self):
        # Le membre emprunte 3 articles via la méthode `emprunter()`
        self.membre.emprunter("livre", self.livre.id)
        self.membre.emprunter("cd", self.cd.id)
        self.membre.emprunter("dvd", self.dvd.id)

        # Vérifier qu'il est bloqué
        self.membre.check_bloque()
        self.assertTrue(self.membre.bloque, "Le membre doit être bloqué après 3 emprunts")

        # Tentative d'un 4ème emprunt (qui devrait échouer)
        success = self.membre.emprunter("livre", self.livre.id)
        self.assertFalse(success, "Le membre ne devrait pas pouvoir emprunter un 4ème article")

        # Vérifier que le nombre d'emprunts reste à 3
        self.assertEqual(self.membre.nb_emprunts(), 3, "Le membre ne devrait pas pouvoir emprunter plus de 3 articles")
