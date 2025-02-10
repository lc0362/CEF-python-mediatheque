from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        """Création d’un utilisateur admin pour l’authentification"""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_login(self.user)

    def test_menu_bibliothecaire(self):
        response = self.client.get(reverse('menuBibliotheque'))
        self.assertEqual(response.status_code, 200)

    def test_add_bibliotheque(self):
        response = self.client.get(reverse('addBibliotheque'))
        self.assertEqual(response.status_code, 200)

    def test_update_bibliotheque(self):
        response = self.client.get(reverse('updateBibliotheque'))
        self.assertEqual(response.status_code, 200)

    def test_loan_management_access(self):
        response = self.client.get(reverse('loan_management'))
        self.assertEqual(response.status_code, 200)
