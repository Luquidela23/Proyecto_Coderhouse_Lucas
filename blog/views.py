

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo
from django.contrib.auth.decorators import login_required
from .forms import ArticuloForm

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'blog/lista_articulos.html', {'articulos': articulos})

def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    return render(request, 'blog/detalle_articulo.html', {'articulo': articulo})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.instance.autor = request.user
            form.save()
            return render(request, 'blog/articulo_creado.html')
    else:
        form = ArticuloForm()

    return render(request, 'blog/crear_articulo.html', {'form': form})

@login_required
def editar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    if request.user == articulo.autor:
        if request.method == 'POST':
            form = ArticuloForm(request.POST, instance=articulo)
            if form.is_valid():
                form.save()
                return redirect('detalle_articulo', articulo_id=articulo.pk)
        else:
            form = ArticuloForm(instance=articulo)
        return render(request, 'blog/editar_articulo.html', {'form': form})
    else:
        return redirect('lista_articulos')

@login_required
def eliminar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    if request.user == articulo.autor:
        articulo.delete()
    return redirect('lista_articulos')