from django.shortcuts import render, redirect
from django.contrib import messages
from bibliothecaire.models import Membre
from bibliothecaire.forms import FormMember

def addMemberBibliotheque(request):
    membres = Membre.objects.all()
    form_member = FormMember()

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