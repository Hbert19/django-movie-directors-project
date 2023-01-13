from django.contrib import admin
from django.urls import path, include
from peliculas import urls as directores
from . import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('directores/', include(directores))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
