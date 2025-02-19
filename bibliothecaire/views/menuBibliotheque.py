from django.shortcuts import render

def menuBibliotheque(request):
    return render(request, "menuBibliotheque.html", {
        "utilisateur": request.user,
        "session": request.session.session_key,
    })

