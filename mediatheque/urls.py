from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('', index, name="index"),
    path('bibliothecaire/', include("bibliothecaire.urls")),
    path('membre/', include("membre.urls")),
    path('admin/', admin.site.urls),
]

