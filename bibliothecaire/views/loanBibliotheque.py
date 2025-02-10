from django.shortcuts import render, get_object_or_404, redirect
from bibliothecaire.models.membre import Emprunteur
from bibliothecaire.models.emprunt import Emprunt
from mediatheque.models import Livre, Cd, Dvd
from django.contrib import messages

def loan_management(request):
    membres = Emprunteur.objects.all()
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()

    if request.method == "POST":
        membre_id = request.POST.get("membre_id")
        item_id = request.POST.get("item_id")
        item_type = request.POST.get("item_type")

        if not membre_id or not item_id or not item_type:
            messages.error(request, "Données manquantes")
            return redirect("loan_management")

        membre = get_object_or_404(Emprunteur, id=membre_id)

        if membre.bloque:
            messages.error(request, "Ce membre a atteint la limite de 3 emprunts.")
            return redirect("loan_management")

        Emprunt.objects.create(membre=membre, item_id=item_id, item_type=item_type)

        membre.check_bloque()
        messages.success(request, f"{item_type.capitalize()} emprunté avec succès !")

        return redirect("loan_management")

    return render(request, "loan.html", {
        "membres": membres,
        "livres": livres,
        "cds": cds,
        "dvds": dvds,
    })

def return_item(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, id=emprunt_id)
    emprunt.give_back()
    messages.success(request, "Emprunt rendu avec succès !")
    return redirect("loan_management")