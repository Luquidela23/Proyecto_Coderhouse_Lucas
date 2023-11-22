from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Perfil

class PerfilForm(UserChangeForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'apellido', 'avatar']
