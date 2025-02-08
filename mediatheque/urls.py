from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .views import index


def bibliothecaire_redirect(request):
    if request.user.is_authenticated:
        return redirect('/bibliothecaire/')
    return redirect('/admin/login/?next=/bibliothecaire/')

urlpatterns = [
    path('', index, name="index"),
    path('bibliothecaire/', include("bibliothecaire.urls")),
    path('bibliothecaire/login/', bibliothecaire_redirect, name='bibliothecaire-login'),
    path('membre/', include("membre.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), #ajout documentation django
]

