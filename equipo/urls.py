from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('prueba/',views.prueba),
    path('actualizar-jugador-modal/',views.ActualizarJugadorModal),
    path('actualizar-proceso/',views.ProcesoActualizar),
    path('nuevo-jugador-modal/',views.nuevoJugadorModal),
    path('crear-nuevo-jugador/',views.ProcesoNuevoJugador),
    path('eliminar-jugado/',views.eliminarJugador)
]