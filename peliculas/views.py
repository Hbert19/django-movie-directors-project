from django.shortcuts import render
from .models import *
from django.utils.text import slugify

def directores(request, director_nombre):
    director_nombre = director_nombre.replace('-', ' ')
    director = Director.objects.filter(nombre=director_nombre).first()
    peliculas = Pelicula.objects.filter(director=director.id)

    return render(request, 'peliculas/directores.html', {
        "peliculas": peliculas,
        "director": director
    })

def peliculas(request):

    peliculas = Pelicula.objects.all().order_by('nombre')

    return render(request, 'peliculas/peliculas.html', {
        "peliculas": peliculas
    })