from django.test import TestCase
from mediatheque.models.media import Livre

class TestMedia(TestCase):
    def test_CreateItem(self):
        livre = Livre.objects.create(name="Test Book", auteur="Test Autor")
        self.assertEqual(Livre.objects.count(), 1)
        self.assertEqual(livre.name, "Test Book")
        self.assertEqual(livre.auteur, "Test Autor")
