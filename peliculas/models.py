from django.db import models
from directores_cine import settings
from django.utils.text import slugify

class Pelicula(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre de la película', blank=True, null=True, max_length=100)
    director = models.ForeignKey(
        'Director', on_delete=models.SET_NULL, null=True)
    genero = models.ManyToManyField('Genero')
    portada = models.ImageField(upload_to="{}{}".format(settings.MEDIA_ROOT, '/portadas'), verbose_name='Portada de la película')
    descripcion = models.TextField(verbose_name='Descripción de la película', max_length=300, null=True)
    año = models.IntegerField(verbose_name='Año de la película', null=True)
    tiempo = models.TimeField(verbose_name='Duración de la película', null=True)

    def generos(self):
        return self.genero.select_related().all() # Esto es para poder llamar a los generos desde el template

    def obtener_portada(self):
        if self.portada:
            return "{}{}".format(settings.MEDIA_URL, self.portada)

    def __str__(self) -> str:

        return self.nombre


class Director(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre del director', max_length=100)
    imagen = models.ImageField(
        verbose_name='Imagen del director', upload_to='{}{}'.format(settings.MEDIA_ROOT, '/directors'))

    def obtener_director(self):
        if self.nombre:
            director = slugify(self.nombre)
            return "{}{}".format('directores/', director)

    def __str__(self) -> str:

        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(
        verbose_name='Genero de la película', max_length=100, unique=True)

    def __str__(self) -> str:

        return self.nombre
