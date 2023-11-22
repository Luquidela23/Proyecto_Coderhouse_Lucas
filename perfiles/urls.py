from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.registro, name='registro'),
    path('login/', views.inicio_sesion, name='inicio_sesion'),
    path('profile/', views.perfil, name='perfil'),
]
