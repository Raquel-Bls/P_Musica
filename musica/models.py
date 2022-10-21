from django.db import models
from django.urls import reverse

# Create your models here.


class Artista(models.Model):
    Nombre = models.CharField(max_length=20)
    Descripcion = models.TextField(max_length=1000)
    Generos = models.TextField(max_length=30)
    Ultimo_lanzamiento = models.TextField(max_length=30)
    Popular_semana = models.TextField(max_length=30)

    def __str__(self) -> str:
        return self.Nombre[:10]

    def get_absolute_url(self):
        return reverse("artista_detalle", args=[str(self.id)])


class EstadoAnimo(models.Model):
    Nom_Estado = models.CharField(max_length=10)
    Descripcion = models.TextField(max_length=1000)
    Canciones = models.CharField(max_length=2000)
    Artista_Esc = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.Nom_Estado[:10]

    def get_absolute_url(self):
        return reverse("estado_animo_detalle", args=[str(self.id)])
