# Generated by Django 4.1.4 on 2022-12-31 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_alter_director_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='imagen',
            field=models.ImageField(upload_to='media/directors/<django.db.models.fields.CharField>.jpg', verbose_name='Imagen del director'),
        ),
    ]
