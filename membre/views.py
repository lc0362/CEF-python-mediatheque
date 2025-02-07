from django.shortcuts import render
from mediatheque.models.media import Livre, Cd, Dvd
from mediatheque.models.jeu import JeuDePlateau

def menuMembre(request):
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, "menuMembre.html", {
        'livres': livres,
        'cds': cds,
        'dvds': dvds,
        'jeux': jeux
    })