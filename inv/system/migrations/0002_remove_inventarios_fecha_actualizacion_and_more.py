# Generated by Django 4.2.6 on 2023-11-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventarios',
            name='fecha_actualizacion',
        ),
        migrations.RemoveField(
            model_name='inventarios',
            name='fecha_creacion',
        ),
        migrations.AlterField(
            model_name='inventarios',
            name='hora_inicio',
            field=models.TimeField(auto_now_add=True),
        ),
    ]