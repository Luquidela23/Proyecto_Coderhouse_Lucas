from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    #imagen = models.ImageField(upload_to='articulo_imagenes/', blank=True, null=True) no tengo la aplicacion necesaria para esto

    def __str__(self):
        return self.titulo