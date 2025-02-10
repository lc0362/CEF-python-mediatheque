from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models.membre import Emprunteur
import re

class TestAddMember(TestCase):

    def test_miss_name(self):
        data = {
            "nom": "",  # Nom manquant
            "prenom": "John",
            "email": "johndoe@gmail.com",
            "telephone": "0600000001",
            "optin": False
        }
        response = self.client.post(reverse('addMemberBibliotheque'), data)
        self.assertRegex(response.content.decode(), re.escape("Ce champ est obligatoire."))

    def test_miss_firstname(self):
        data = {
            "nom": "Doe",
            "prenom": "",  # Prénom manquant
            "email": "johndoe@gmail.com",
            "telephone": "0600000001",
            "optin": False
        }
        response = self.client.post(reverse('addMemberBibliotheque'), data)
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
        self.assertRegex(response.content.decode(), re.escape("Ce champ est obligatoire."))

    def test_add_member(self):
        """Test ajout d’un membre"""
        data = {
            "nom": "Nomtest",
            "prenom": "Prenomtest",
            "email": "example@example.com",
            "telephone": "0600000001"
        }
        response = self.client.post(reverse('addMemberBibliotheque'), data)
        self.assertEqual(response.status_code, 302)

class TestUpdateMember(TestCase):
    def setUp(self):
        """Création d’un emprunteur pour le test"""
        self.membre = Emprunteur.objects.create(nom="Doe", prenom="John", email="johndoe@gmail.com", telephone="0600000000", optin=False)

    def test_update_member(self):
        """Test mise à jour d’un membre"""
        self.assertEqual(self.membre.telephone, "0600000000")

        data = {
            "nom": self.membre.nom,
            "prenom": self.membre.prenom,
            "email": self.membre.email,
            "telephone": "0600000001",  # Nouveau numéro
            "optin": self.membre.optin,
            "modif_membre": self.membre.id
        }

        response = self.client.post(reverse('updateMemberBibliotheque'), data)
        self.assertEqual(response.status_code, 302)

        # Rafraîchir l'objet depuis la BDD
        self.membre.refresh_from_db()

        # Vérifier que la modification a bien été prise en compte
        self.assertEqual(self.membre.telephone, "0600000001")
