# Generated by Django 4.1.6 on 2023-02-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posiciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.CharField(max_length=100)),
            ],
        ),
    ]