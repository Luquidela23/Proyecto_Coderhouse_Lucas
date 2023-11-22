from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.articulo_lista, name='articulo_lista'),
    path('pages/<int:articulo_id>/', views.detalle_articulo, name='detalle_articulo'),
    path('pages/nuevo/', views.crear_articulo, name='crear_articulo'),
    path('pages/editar/<int:articulo_id>/', views.editar_articulo, name='editar_articulo'),
    path('pages/borrar/<int:articulo_id>/', views.borrar_articulo, name='borrar_articulo'),
]
