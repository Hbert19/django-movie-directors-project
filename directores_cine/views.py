from django.shortcuts import render
from peliculas.models import Director
from django.utils.text import slugify

def index(request):

    directores = Director.objects.all()

    return render(request, 'index.html', {
        "directores": directores
    })