from django import forms
from mediatheque.models.jeu import JeuDePlateau
from mediatheque.models.media import Livre, Cd, Dvd
from django.http import JsonResponse

class FormLivres(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['name', 'auteur']

class FormDvds(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = ['name', 'realisateur']

class FormCds(forms.ModelForm):
    class Meta:
        model = Cd
        fields = ['name', 'artiste']

class FormJeux(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ['name', 'createur']

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

def delete_item(request, item_type, item_id):
    model_map = {
        'livre': Livre,
        'cd': Cd,
        'dvd': Dvd,
        'jeu': JeuDePlateau
    }

    if item_type in model_map:
        item = get_object_or_404(model_map[item_type], pk=item_id)
        item.delete()
        return JsonResponse({'success': True, 'item_id': item_id, 'item_type': item_type})
    else:
        return JsonResponse({'success': False, 'error': "Type d'article invalide"}, status=400)
