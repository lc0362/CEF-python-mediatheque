from django.contrib import admin
from mediatheque.models.jeu import JeuDePlateau
from mediatheque.models.media import Livre, Dvd, Cd
from bibliothecaire.models.membre import Emprunteur

admin.site.register(JeuDePlateau)
admin.site.register(Livre)
admin.site.register(Dvd)
admin.site.register(Cd)
admin.site.register(Emprunteur)
