from django import forms
from bibliothecaire.models import Membre

class FormMember(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['nom', 'prenom', 'email', 'optin', 'telephone']

