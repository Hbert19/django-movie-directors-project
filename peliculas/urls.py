from django.urls import path
from . import views

urlpatterns = [
    path('', views.directores, name='directores'), # Vista para todas las peliculas
    path('todas-las-peliculas/', views.peliculas, name='peliculas'),
    path('<str:director_nombre>/', views.directores, name='directores')
]