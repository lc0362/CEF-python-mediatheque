from django import forms
from bibliothecaire.models import Membre

class UpdateMembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['nom', 'prenom', 'email', 'telephone', 'optin']
