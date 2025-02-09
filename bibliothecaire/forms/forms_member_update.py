from django import forms
from bibliothecaire.models import Emprunteur

class UpdateMembreForm(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['nom', 'prenom', 'email', 'telephone', 'optin']
