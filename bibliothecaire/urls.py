from django.urls import path
from .views import menuBibliotheque, addBibliotheque, updateBibliotheque, delete_item, addMemberBibliotheque

urlpatterns = [
    path('', menuBibliotheque, name="menuBibliotheque"),
    path('add/', addBibliotheque, name="addBibliotheque"),
    path('update/', updateBibliotheque, name="updateBibliotheque"),
    path('delete/<str:item_type>/<int:item_id>/', delete_item, name="delete_item"),
    path('add-member/', addMemberBibliotheque, name="addMemberBibliotheque"),
]
