"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from mediatheque.models.jeu import JeuDePlateau
from mediatheque.models.media import Livre, Cd, Dvd
from .forms import FormJeux, FormLivres, FormCds, FormDvds, UpdateLivreForm, UpdateCdForm, UpdateDvdForm, UpdateJeuForm
from django.contrib.auth.decorators import login_required

@login_required
def menuBibliotheque(request):
    return render(request, "menuBibliotheque.html")

def addBibliotheque(request):
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    jeux = JeuDePlateau.objects.all()
    form_livres = FormLivres()
    form_jeux = FormJeux()
    form_cds = FormCds()
    form_dvds = FormDvds()

    if request.method == 'POST':
        if 'ajout_livre' in request.POST:
            form_livres = FormLivres(request.POST)
            if form_livres.is_valid():
                form_livres.save()
                messages.success(request, "Livre ajouté avec succès !")
                return redirect('addBibliotheque')

        elif 'ajout_jeu' in request.POST:
            form_jeux = FormJeux(request.POST)
            if form_jeux.is_valid():
                form_jeux.save()
                messages.success(request, "Jeu ajouté avec succès !")
                return redirect('addBibliotheque')

        elif 'ajout_cd' in request.POST:
            form_cds = FormCds(request.POST)
            if form_cds.is_valid():
                form_cds.save()
                messages.success(request, "CD ajouté avec succès !")
                return redirect('addBibliotheque')

        elif 'ajout_dvd' in request.POST:
            form_dvds = FormDvds(request.POST)
            if form_dvds.is_valid():
                form_dvds.save()
                messages.success(request, "DVD ajouté avec succès !")
                return redirect('addBibliotheque')

    dictionnaire = {
        "livres": livres,
        "dvds": dvds,
        "cds": cds,
        "jeux": jeux,
        "form_livres": form_livres,
        "form_jeux": form_jeux,
        "form_cds": form_cds,
        "form_dvds": form_dvds,
    }

    return render(request, "addBibliotheque.html", dictionnaire)

def updateBibliotheque(request):
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    jeux = JeuDePlateau.objects.all()

    update_forms = {
        'livre': [(livre.id, UpdateLivreForm(instance=livre)) for livre in livres],
        'dvd': [(dvd.id, UpdateDvdForm(instance=dvd)) for dvd in dvds],
        'cd': [(cd.id, UpdateCdForm(instance=cd)) for cd in cds],
        'jeu': [(jeu.id, UpdateJeuForm(instance=jeu)) for jeu in jeux],
    }

    if request.method == 'POST':
        item_types = ['livre', 'dvd', 'cd', 'jeu']
        for item_type in item_types:
            item_id = request.POST.get(f'modif_{item_type}')
            if item_id:
                model_map = {
                    'livre': (Livre, UpdateLivreForm),
                    'dvd': (Dvd, UpdateDvdForm),
                    'cd': (Cd, UpdateCdForm),
                    'jeu': (JeuDePlateau, UpdateJeuForm),
                }
                model, form_class = model_map.get(item_type, (None, None))

                if model and form_class:
                    item = get_object_or_404(model, pk=item_id)
                    form = form_class(request.POST, instance=item)
                    if form.is_valid():
                        form.save()
                        messages.success(request, f"{item_type.capitalize()} modifié avec succès !")
                        return redirect('updateBibliotheque')

    dictionnaire = {
        "livres": livres,
        "dvds": dvds,
        "cds": cds,
        "jeux": jeux,
        "update_forms_livres": update_forms['livre'],
        "update_forms_dvds": update_forms['dvd'],
        "update_forms_cds": update_forms['cd'],
        "update_forms_jeux": update_forms['jeu'],
    }

    return render(request, "updateBibliotheque.html", dictionnaire)

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
"""