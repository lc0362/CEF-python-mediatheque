from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def menuBibliotheque(request):
    return render(request, "menuBibliotheque.html")
