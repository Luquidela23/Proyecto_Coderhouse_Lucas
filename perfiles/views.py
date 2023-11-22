from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm

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
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('articulo_lista')
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