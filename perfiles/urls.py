from django.urls import path
from .views import registro, inicio_sesion, perfil, editar_perfil

urlpatterns = [
    path('signup/', registro, name='registro'),
    path('login/', inicio_sesion, name='inicio_sesion'),
    path('profile/', perfil, name='perfil'),
    path('edit-profile/', editar_perfil, name='editar_perfil')
]