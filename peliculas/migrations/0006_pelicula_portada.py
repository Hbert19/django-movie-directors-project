# Generated by Django 4.1.4 on 2022-12-31 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0005_alter_director_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(default='null', upload_to='media/portadas/', verbose_name='Portada de la película'),
            preserve_default=False,
        ),
    ]
