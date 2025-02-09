from django import forms
from bibliothecaire.models.membre import Emprunteur

class FormMember(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['nom', 'prenom', 'email', 'optin', 'telephone']

