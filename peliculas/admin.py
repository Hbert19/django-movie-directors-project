from django.contrib import admin
from .models import *
from decimal import Decimal

class PeliculaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'director',
        'portada',
        'duracion',
        'año'
    )

    def duracion(self, obj) -> str:
        return str(obj.tiempo)[1:2] + "h" + str(obj.tiempo)[2:5] + "m"

    class Meta():
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'


class DirectorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'imagen'
    )

    class Meta():
        verbose_name = 'Director'
        verbose_name_plural = 'Directores'


class GeneroAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
    )

    class Meta():
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'


admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genero, GeneroAdmin)
