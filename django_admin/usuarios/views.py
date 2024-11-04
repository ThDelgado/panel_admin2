from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from .forms import RegistroUsuarioForm, LoginUsuarioForm

from app_libros.models import Libros
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.


def registro_view(request):
    form = None
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            
            content_type = ContentType.objects.get_for_model(Libros)
            
            # obtenemos el permiso a asignar
            permiso = Permission.objects.get(codename='development')
        
            user = form.save() 
            user.user_permissions.add(permiso)
            login(request, user)
            
            messages.success(request, f"Usuario {user.username} registrado con éxito.")
            return redirect('home')
        else:
            messages.error(request, "Error al intentar registrar al usuario, por favor verifique los datos.")
            return render(request, 'usuarios/registro.html', {"form": form})
                
    else:
        form = RegistroUsuarioForm()
        return render(request, 'usuarios/registro.html', {"form": form})


def login_view(request):
    
    form = LoginUsuarioForm()
    
    if request.method == "POST":
        form = LoginUsuarioForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username= username, password= password)
         
            if user is not None:
                login(request, user)
                return redirect("home")
            
        else:
            form.add_error(None, "Formulario invalido, Por favor,  revise los campos")

    return render(request, 'usuarios/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')