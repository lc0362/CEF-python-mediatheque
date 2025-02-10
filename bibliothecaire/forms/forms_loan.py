from django import forms

class FormLoan(forms.Form):
    item_type = forms.ChoiceField(
        choices=[('livre', 'Livre'), ('cd', 'CD'), ('dvd', 'DVD')],
        widget=forms.HiddenInput()
    )
    item_id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        from bibliothecaire.models.membre import Emprunteur  # Import local
        super().__init__(*args, **kwargs)
        self.fields['membre'] = forms.ModelChoiceField(queryset=Emprunteur.objects.all(), label="Membre")
