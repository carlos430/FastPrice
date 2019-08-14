from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Articulo
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

#Aqui se pone la direccion de donde esta el archivo HTML,
#Recuerda ponerlo dentro del template.


def inicio(request):
	queryset = request.GET.get("titulo")
	articulos = Articulo.objects.filter(nombres = True)
	if queryset:
		articulos = Articulo.objects.filter(
			Q(nombres__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
	return render(request, 'blog/index.html',{'articulos':articulos})
	
def registrar(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"Nueva Cuenta Creada: {username}")
			login(request, user)
			messages.info(request, f"Haz iniciado sesión como {username}")
			return redirect("inicio")

		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
			
	form = NewUserForm
	return render(request, 
					'blog/registrar.html', 
					 context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Sesión Finalizada Exitosamente")
	return redirect("inicio")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Haz iniciado sesión como {username}")
				return redirect("inicio")
			else:
				messages.error(request, "Usuario o Contraseña invalida")
	form = AuthenticationForm()
	return render(request,
					"blog/login.html",
					{"form":form})
