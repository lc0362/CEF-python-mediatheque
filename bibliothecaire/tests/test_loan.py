import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mediatheque.settings')
django.setup()

from django.test import TestCase
from django.urls import reverse
from mediatheque.models.media import Livre, Cd, Dvd

class TestLoanSystem(TestCase):
    def setUp(self):
        """Réinitialise la base de données pour éviter les conflits"""
        Membre.objects.all().delete()
        Livre.objects.all().delete()
        Cd.objects.all().delete()
        Dvd.objects.all().delete()

        # Création d'un membre
        self.membre = Membre.objects.create(
            nom="Doe",
            prenom="John",
            email="johndoe@gmail.com",
            telephone="0600000000",
            optin=False
        )

        # Création d'articles empruntables
        self.livre = Livre.objects.create(name="Livre Test", auteur="Auteur Test")
        self.cd = Cd.objects.create(name="CD Test", artiste="Artiste Test")
        self.dvd = Dvd.objects.create(name="DVD Test", realisateur="Réalisateur Test")

    def test_loan_book(self):
        """ Vérifie qu'un livre peut être emprunté par un membre """
        response = self.client.post(reverse('loan_management'), {
            'membre_id': self.membre.id,
            'item_id': self.livre.id,
            'item_type': 'livre'
        })
        self.assertEqual(response.status_code, 200)  # Vérifie la réponse HTTP
        self.assertIn("success", response.json())  # Vérifie si la réponse contient "success"

    def test_loan_cd(self):
        """ Vérifie qu'un CD peut être emprunté par un membre """
        response = self.client.post(reverse('loan_management'), {
            'membre_id': self.membre.id,
            'item_id': self.cd.id,
            'item_type': 'cd'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.json())

    def test_loan_dvd(self):
        """ Vérifie qu'un DVD peut être emprunté par un membre """
        response = self.client.post(reverse('loan_management'), {
            'membre_id': self.membre.id,
            'item_id': self.dvd.id,
            'item_type': 'dvd'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.json())
