# Generated by Django 4.2.16 on 2024-11-03 21:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_libros', '0004_alter_libros_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libros',
            options={'permissions': [('development', 'Desarrolladorls')]},
        ),
        migrations.AddField(
            model_name='libros',
            name='fecha_publicacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]