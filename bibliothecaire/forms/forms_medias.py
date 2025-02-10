from django import forms
from mediatheque.models import Livre, Cd, Dvd, JeuDePlateau

class FormLivres(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['name', 'auteur']

class FormCds(forms.ModelForm):
    class Meta:
        model = Cd
        fields = ['name', 'artiste']

class FormDvds(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = ['name', 'realisateur']

class FormJeux(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ['name', 'createur']
