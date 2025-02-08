from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Membre
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

        # Vérifie si le message "Ce champ est obligatoire." est dans une liste d'erreurs
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

        # Vérifie si le message "Ce champ est obligatoire." est dans une liste d'erreurs
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

        # Vérifie si le message "Ce champ est obligatoire." est dans une liste d'erreurs
        self.assertRegex(response.content.decode(), re.escape("Ce champ est obligatoire."))

class TestUpdateMember(TestCase):
    def setUp(self):
        self.membre = Membre.objects.create(nom="Doe", prenom="John", email="johndoe@gmail.com", telephone="0600000000", optin=False)

    def test_update_member(self):
        """
        Vérifie qu'on peut modifier un membre.
        """
        # Vérifier la valeur initiale du téléphone
        self.assertEqual(self.membre.telephone, "0600000000")

        # Préparation des données de mise à jour
        data = {
            "nom": self.membre.nom,
            "prenom": self.membre.prenom,
            "email": self.membre.email,
            "telephone": "0600000001",  # Nouveau numéro
            "optin": self.membre.optin,
            "modif_membre": self.membre.id
        }

        # Effectuer la requête POST pour modifier le membre
        response = self.client.post(reverse('updateMemberBibliotheque'), data)

        # Vérifier que la vue redirige bien (HTTP 302)
        self.assertEqual(response.status_code, 302)

        # Rafraichi l'objet depuis la BDD
        self.membre.refresh_from_db()

        # Vérifier que la modification a bien été prise en compte
        self.assertEqual(self.membre.telephone, "0600000001")

    def test_delete_member(self):
        """
        Vérifie qu'on peut supprimer un membre.
        """
        response = self.client.post(reverse('delete_member', args=[self.membre.id]))
        self.assertEqual(Membre.objects.count(), 0)