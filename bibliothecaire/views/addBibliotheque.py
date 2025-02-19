from django.shortcuts import render, redirect
from django.contrib import messages
from mediatheque.models import Livre, Cd, Dvd, JeuDePlateau
from bibliothecaire.forms.forms_medias import FormLivres, FormCds, FormDvds, FormJeux

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
        form_map = {
            'ajout_livre': (form_livres, FormLivres),
            'ajout_jeu': (form_jeux, FormJeux),
            'ajout_cd': (form_cds, FormCds),
            'ajout_dvd': (form_dvds, FormDvds),
        }

        for key, (form_instance, form_class) in form_map.items():
            if key in request.POST:
                form = form_class(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, f"{key.split('_')[1].capitalize()} ajouté avec succès !")
                    return redirect('addBibliotheque')

    return render(request, "addBibliotheque.html", {
        "livres": livres, "dvds": dvds, "cds": cds, "jeux": jeux,
        "form_livres": form_livres, "form_jeux": form_jeux, "form_cds": form_cds, "form_dvds": form_dvds,
    })
