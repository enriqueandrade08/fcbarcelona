# Generated by Django 4.1.6 on 2023-02-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_posiciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugadores',
            name='estado',
            field=models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1),
        ),
    ]
