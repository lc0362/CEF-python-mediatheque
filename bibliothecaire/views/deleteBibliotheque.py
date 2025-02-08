from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from mediatheque.models.media import Livre, Cd, Dvd
from mediatheque.models.jeu import JeuDePlateau

@csrf_protect
def delete_item(request, item_type, item_id):
    model_map = {
        'livre': Livre,
        'cd': Cd,
        'dvd': Dvd,
        'jeu': JeuDePlateau
    }

    if item_type not in model_map:
        return JsonResponse({'success': False, 'error': "Type d'article invalide"}, status=400)

    item = get_object_or_404(model_map[item_type], pk=item_id)

    if request.method == 'POST':
        item.delete()
        return JsonResponse({'success': True, 'item_id': item_id, 'item_type': item_type})

    return JsonResponse({'success': False, 'error': "Méthode non autorisée"}, status=405)
