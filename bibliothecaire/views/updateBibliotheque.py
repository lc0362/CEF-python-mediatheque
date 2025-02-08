from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from mediatheque.models.media import Livre, Cd, Dvd
from mediatheque.models.jeu import JeuDePlateau
from bibliothecaire.forms.forms_update import UpdateLivreForm, UpdateCdForm, UpdateDvdForm, UpdateJeuForm

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
        model_map = {
            'livre': (Livre, UpdateLivreForm),
            'dvd': (Dvd, UpdateDvdForm),
            'cd': (Cd, UpdateCdForm),
            'jeu': (JeuDePlateau, UpdateJeuForm),
        }

        for item_type, (model, form_class) in model_map.items():
            item_id = request.POST.get(f'modif_{item_type}')
            if item_id:
                item = get_object_or_404(model, pk=item_id)
                form = form_class(request.POST, instance=item)
                if form.is_valid():
                    form.save()
                    messages.success(request, f"{item_type.capitalize()} modifié avec succès !")
                    return redirect('updateBibliotheque')

    return render(request, "updateBibliotheque.html", {
        "livres": livres, "dvds": dvds, "cds": cds, "jeux": jeux,
        "update_forms_livres": update_forms['livre'],
        "update_forms_dvds": update_forms['dvd'],
        "update_forms_cds": update_forms['cd'],
        "update_forms_jeux": update_forms['jeu'],
    })
