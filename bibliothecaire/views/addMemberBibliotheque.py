from django.shortcuts import render, redirect
from django.contrib import messages
from bibliothecaire.models.membre import Emprunteur
from bibliothecaire.forms import FormMember

def addMemberBibliotheque(request):
    membres = Emprunteur.objects.all()
    form_member = FormMember(request.POST or None)  

    if request.method == 'POST':
        if form_member.is_valid():
            form_member.save()
            messages.success(request, "Membre ajouté avec succès !")
            return redirect('addMemberBibliotheque')
        else:
            print("🔴 Erreurs du formulaire:", form_member.errors)  # Débogage


    return render(request, "addMemberBibliotheque.html", {
        "membres": membres,
        "form_member": form_member,  
    })
