from django.urls import path
from .views import (
    menuBibliotheque,
    addBibliotheque,
    updateBibliotheque,
    delete_item,
    addMemberBibliotheque,
    updateMemberBibliotheque,
    delete_member
    )

urlpatterns = [
    path('', menuBibliotheque, name="menuBibliotheque"),
    path('add/', addBibliotheque, name="addBibliotheque"),
    path('update/', updateBibliotheque, name="updateBibliotheque"),
    path('delete/<str:item_type>/<int:item_id>/', delete_item, name="delete_item"),
    path('add-member/', addMemberBibliotheque, name="addMemberBibliotheque"),
    path('update-member/', updateMemberBibliotheque, name="updateMemberBibliotheque"),
    path('delete-member/<int:membre_id>/', delete_member, name="delete_member"),
]
