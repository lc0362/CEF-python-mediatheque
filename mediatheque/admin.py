from django.contrib import admin
from .models.jeu import JeuDePlateau
from .models.media import Livre, Dvd, Cd

admin.site.register(JeuDePlateau)
admin.site.register(Livre)
admin.site.register(Dvd)
admin.site.register(Cd)
