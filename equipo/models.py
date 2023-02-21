from django.db import models

# Create your models here.
from django.db import models

class Jugadores(models.Model):
    OPCION_ACTIVO = 'A'
    OPCION_INACTIVO = 'I'
    OPCIONES_ESTADO = [
        (OPCION_ACTIVO, 'Activo'),
        (OPCION_INACTIVO, 'Inactivo')
    ]

    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    numero = models.IntegerField()
    fecha_nacimiento = models.DateField()
    estado = models.CharField(max_length=1, choices=OPCIONES_ESTADO, default=OPCION_ACTIVO)

class Posiciones(models.Model):
    posicion = models.CharField(max_length=100)