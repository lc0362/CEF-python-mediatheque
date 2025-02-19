from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .views import (
    menuBibliotheque,
    addBibliotheque,
    updateBibliotheque,
    delete_item,
    addMemberBibliotheque,
    updateMemberBibliotheque,
    delete_member,
    loan_management,
    return_item,
    BibliothecaireLoginView,
)

def bibliothecaire_redirect(request):
    if not request.user.is_authenticated:
        return redirect('/bibliothecaire/login/')
    return menuBibliotheque(request)

urlpatterns = [
    path('', login_required(menuBibliotheque, login_url='/bibliothecaire/login/'), name="menuBibliotheque"),
    path('add/', login_required(addBibliotheque, login_url='/bibliothecaire/login/'), name="addBibliotheque"),
    path('update/', login_required(updateBibliotheque, login_url='/bibliothecaire/login/'), name="updateBibliotheque"),
    path('delete/<str:item_type>/<int:item_id>/', login_required(delete_item, login_url='/bibliothecaire/login/'), name="delete_item"),
    path('add-member/', login_required(addMemberBibliotheque, login_url='/bibliothecaire/login/'), name="addMemberBibliotheque"),
    path('update-member/', login_required(updateMemberBibliotheque, login_url='/bibliothecaire/login/'), name="updateMemberBibliotheque"),
    path('delete-member/<int:membre_id>/', login_required(delete_member, login_url='/bibliothecaire/login/'), name="delete_member"),
    path('loan/', login_required(loan_management, login_url='/bibliothecaire/login/'), name="loan_management"),
    path("return/<int:emprunt_id>/", login_required(return_item, login_url='/bibliothecaire/login/'), name="return_item"),
    path('login/', BibliothecaireLoginView.as_view(), name="bibliothecaire-login"),
]
