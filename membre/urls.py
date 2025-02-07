from django.urls import path
from .views import menuMembre

urlpatterns = [
    path('', menuMembre, name="menuMembre"),
]