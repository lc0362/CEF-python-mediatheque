from django.shortcuts import render, redirect
from django.contrib import messages
from bibliothecaire.models.membre import Emprunteur
from bibliothecaire.forms import FormMember

def addMemberBibliotheque(request):
    membres = Emprunteur.objects.all()
    form_member = FormMember(request.POST or None)

    if request.method == 'POST':
        form = FormMember(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Membre ajouté avec succès !")
            return redirect('addMemberBibliotheque')

    return render(request, "addMemberBibliotheque.html", {
        "membres": membres,
        "form_member": form_member,
    })