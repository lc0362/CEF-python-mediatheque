from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from bibliothecaire.models import Emprunteur

def delete_member(request, membre_id):
    membre = get_object_or_404(Emprunteur, pk=membre_id)
    membre.delete()
    return JsonResponse({'success': True, 'membre_id': membre_id})
