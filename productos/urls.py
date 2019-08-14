from django.urls import path
from . import views
from .views import inicio, registrar
from django.conf import settings
from django.conf.urls.static import static

#Este archivo url se debe hacer dentro del archivo de la app.
#Aqui se pone un nombre a la vista, y donde dice NAME se pone el nombre
#de la funcion de views.


urlpatterns = [
	#path("", views.inicio, name="inicio"),
	path("", views.inicio, name="inicio"),
	path("registrar/", views.registrar, name="registrar"),
	path("logout/", views.logout_request, name="logout"),
	path("login/", views.login_request, name="login"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)