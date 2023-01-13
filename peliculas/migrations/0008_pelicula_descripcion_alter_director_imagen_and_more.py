# Generated by Django 4.1.4 on 2023-01-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0007_alter_genero_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='descripcion',
            field=models.TextField(max_length=300, null=True, verbose_name='Descripción de la película'),
        ),
        migrations.AlterField(
            model_name='director',
            name='imagen',
            field=models.ImageField(upload_to='directors/', verbose_name='Imagen del director'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(upload_to='portadas/', verbose_name='Portada de la película'),
        ),
    ]