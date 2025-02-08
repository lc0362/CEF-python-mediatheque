from django import forms
from mediatheque.models.media import Livre, Cd, Dvd
from mediatheque.models.jeu import JeuDePlateau

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
