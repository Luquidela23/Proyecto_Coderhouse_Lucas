

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm
from django.contrib.auth import logout
from .models import Perfil

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio_sesion')
    else:
        form = UserCreationForm()
    return render(request, 'perfiles/registro.html', {'form': form})

def inicio_sesion(request):
    # Obtener el parámetro opcional 'next' de la URL
    next_page = request.GET.get('next', 'lista_articulos')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Iniciar sesión
            login(request, form.get_user())

            # Redirigir a la página indicada por 'next'
            return redirect(next_page)
    else:
        form = AuthenticationForm()

    return render(request, 'perfiles/inicio_sesion.html', {'form': form})

@login_required
def perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if form.is_valid():
            form.save()
    else:
        form = PerfilForm(instance=request.user.perfil)
    return render(request, 'perfiles/perfil.html', {'form': form})


@login_required
def editar_perfil(request):
    # Obtener o crear el perfil del usuario
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'perfiles/editar_perfil.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')