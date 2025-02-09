from django.shortcuts import render, get_object_or_404
from bibliothecaire.models import Emprunteur, Emprunt
from mediatheque.models.media import Livre, Cd, Dvd

def loan_management(request):
    membres = Emprunteur.objects.all()
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()

    if request.method == "POST":
        membre_id = request.POST.get("membre_id")
        item_id = request.POST.get("item_id")
        item_type = request.POST.get("item_type")

        # Vérification des données
        if not membre_id or not item_id or not item_type:
            messages.error(request, "Données manquantes")
            return redirect("loan_management")

        # Récupération du membre
        membre = get_object_or_404(Membre, id=membre_id)

        # Vérifier s'il est bloqué
        if membre.bloque:
            messages.error(request, "Ce membre a atteint la limite de 3 emprunts.")
            return redirect("loan_management")

        # Créer un nouvel emprunt
        Emprunt.objects.create(membre=membre, item_id=item_id, item_type=item_type)

        # Mettre à jour le statut du membre
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