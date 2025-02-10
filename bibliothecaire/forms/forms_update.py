from django import forms
from mediatheque.models import Livre, Cd, Dvd, JeuDePlateau

class UpdateLivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['name', 'auteur']

class UpdateCdForm(forms.ModelForm):
    class Meta:
        model = Cd
        fields = ['name', 'artiste']

class UpdateDvdForm(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = ['name', 'realisateur']

class UpdateJeuForm(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ['name', 'createur']
