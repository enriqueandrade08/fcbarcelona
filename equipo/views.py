from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# from django.urls import reverse
# Importacion de modelos
from .models import Jugadores, Posiciones

# Create your views here.
def index(request):
    titulo = 'Fc Barcelona'
    lista = list(Jugadores.objects.values())
    return render(request,'index.html',{
        'lista' : lista,
        'titulo': titulo
    })

def prueba(request):
    mydata = Jugadores.objects.all()
    return render(request,'prueba.html',{
        'mydata' : mydata
    })

def ActualizarJugadorModal(request):
    if request.method == 'POST':
        id = request.POST.get('variable')
        obj = Jugadores.objects.get(id=id)
        posiciones = Posiciones.objects.all()
        return render(request, 'actualizar-jugador-modal.html',{
            'id':id,
            'datos':obj,
            'posiciones':posiciones
        })

def ProcesoActualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        jugador = Jugadores.objects.get(id=id)
        jugador.nombre = request.POST.get('nombre')
        jugador.posicion = request.POST.get('posicion')
        jugador.numero = request.POST.get('numero')
        jugador.save()
        respuestaScript = "<script>swal('Actualizado', 'Campos actualizados con exito', 'success').then(()=>{window.location.href = ''});</script>"
        response = HttpResponse(respuestaScript, content_type='application/javascript')
        return response

def nuevoJugadorModal(request):
    posiciones = Posiciones.objects.all()
    numero = range(1,25)
    jugadoresNumeros = Jugadores.objects.all()
    return render(request, 'nuevo-jugador-modal.html',{
        'posiciones':posiciones,
        'numeros':numero,
        'jugadores' : jugadoresNumeros
    })

def ProcesoNuevoJugador(request):
    if request.method == 'POST':
        # Capturar los datos
        nombre = request.POST.get('nombre')
        posicion = request.POST.get('posicion')
        numero = request.POST.get('numero')
        fecha_nacimiento = request.POST.get('fecha')
        estado = 'A'
        # Instancia para agregarlas a la bd
        jugador = Jugadores(nombre=nombre, posicion=posicion, numero=numero, fecha_nacimiento=fecha_nacimiento, estado=estado)
        jugador.save()
        respuestaScript = "<script>swal('Actualizado', 'Campos actualizados con exito', 'success').then(()=>{window.location.href = ''});</script>"
        response = HttpResponse(respuestaScript, content_type='application/javascript')
        return response

def eliminarJugador(request):
    if request.method == 'POST':
        # Capturar
        id = request.POST.get('variable')
        # Llamar segun su id
        jugador = Jugadores.objects.get(id=id)
        jugador.estado = 'I' #cambiar estado
        jugador.save() #guardar cambios
        respuestaScript = "<script>swal('Actualizado', 'Jugador eliminado con exito', 'success').then(()=>{window.location.href = ''});</script>"
        response = HttpResponse(respuestaScript, content_type='application/javascript')
        return response