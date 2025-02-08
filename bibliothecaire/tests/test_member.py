from django.test import TestCase
from django.urls import reverse
import re

class TestAddMember(TestCase):

    def test_miss_name(self):
        data = {
            "nom": "", # Nom manquant
            "prenom": "John",
            "email": "johndoe@gmail.com",
            "telephone": "0600000001",
            "optin": False
        }
        response = self.client.post(reverse('addMemberBibliotheque'), data)

        # 🔍 Vérifie si le message "Ce champ est obligatoire." est dans une liste d'erreurs
        self.assertRegex(response.content.decode(), re.escape("Ce champ est obligatoire."))

    def test_miss_firstname(self):
        data = {
            "nom": "Doe",
            "prenom": "",# Prénom manquant
            "email": "johndoe@gmail.com",
            "telephone": "0600000001",
            "optin": False
        }
        response = self.client.post(reverse('addMemberBibliotheque'), data)

        # 🔍 Vérifie si le message "Ce champ est obligatoire." est dans une liste d'erreurs
        self.assertRegex(response.content.decode(), re.escape("Ce champ est obligatoire."))

    def test_miss_email(self):
        data = {
            "nom": "Doe",
            "prenom": "John",
            "email": "",  # Email manquant
            "telephone": "0600000001",
            "optin": False
        }
        response = self.client.post(reverse('addMemberBibliotheque'), data)

        # 🔍 Vérifie si le message "Ce champ est obligatoire." est dans une liste d'erreurs
        self.assertRegex(response.content.decode(), re.escape("Ce champ est obligatoire."))