from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from bibliothecaire.models import Emprunteur
from bibliothecaire.forms.forms_member_update import UpdateMembreForm

def updateMemberBibliotheque(request):
    membres = Emprunteur.objects.all()
    update_forms_membres = {
        membre: UpdateMembreForm(instance=membre) for membre in membres
    }

    if request.method == 'POST':
        membre_id = request.POST.get('modif_membre')
        if membre_id:
            membre = get_object_or_404(Emprunteur, pk=membre_id)
            form = UpdateMembreForm(request.POST, instance=membre)
            if form.is_valid():
                form.save()
                messages.success(request, "Membre modifié avec succès !")
                return redirect('updateMemberBibliotheque')

    return render(request, "updateMemberBibliotheque.html", {
        "membres": update_forms_membres.keys(),
        "update_forms_membres": update_forms_membres,
    })

