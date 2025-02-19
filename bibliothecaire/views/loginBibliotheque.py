from django.contrib.auth.views import LoginView

class BibliothecaireLoginView(LoginView):
    template_name = "login.html"
