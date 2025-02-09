from django import forms
from bibliothecaire.models import Emprunteur

class FormLoan(forms.Form):
    item_type = forms.ChoiceField(
        choices=[('livre', 'Livre'), ('cd', 'CD'), ('dvd', 'DVD')],
        widget=forms.HiddenInput()
    )
    item_id = forms.IntegerField(widget=forms.HiddenInput())
    membre = forms.ModelChoiceField(queryset=Emprunteur.objects.all(), label="Membre")
