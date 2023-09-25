from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #Permite a otros dominio acceder a los metodos
from rest_framework.parsers import JSONParser #Analizar los datos JSON
from django.http.response import JsonResponse #Respuestas de datos JSON


#Datos entrantes
from TiendaAPP.models import RegistroTienda
from TiendaAPP.serializers import RegistroTiendaSerializer

from django.http import HttpResponseRedirect,HttpResponseBadRequest, HttpResponseNotFound



# Create your views here.
@csrf_exempt
def registroTiendaApi(request, id=0):
    if request.session.get('is_authenticated'):
        #devolvera todos los registros en formato JSON
        if request.method=='GET':
            registroTienda = RegistroTienda.objects.all()
            registroTienda_serializer=RegistroTiendaSerializer(registroTienda,many=True)#Uso de clase serializer para convertirlo a formato JSON
            return JsonResponse(registroTienda_serializer.data,safe=False)
        
        
        #Insertar registros en la tabla
        elif request.method=='POST':
            registroTienda_data=JSONParser().parse(request)
            registroTiendaSerializer=RegistroTiendaSerializer(data=registroTienda_data)
            if registroTiendaSerializer.is_valid():
                registroTiendaSerializer.save()
                return JsonResponse("Added Successfully",safe=False)
            return JsonResponse("Failed to Add",safe=False)
        
        
        #Actualizar registro de la tabla
        elif request.method=="PUT":
            registroTienda_data=JSONParser().parse(request)

            registroTienda_id = registroTienda_data['RegistroTiendaId']

            try:
                registroTienda = RegistroTienda.objects.get(RegistroTiendaId=registroTienda_id)
            except RegistroTienda.DoesNotExist:
                return JsonResponse("El registro no existe", safe=False, status=404)

            # Verificar si el usuario que realiza la solicitud es el vendedor
            if registroTienda.id_vendedor == request.session.get('username'):
                # Si el usuario es el vendedor, realiza las actualizaciones necesarias
                registroTienda_serializer = RegistroTiendaSerializer(registroTienda, data=registroTienda_data)
            else:
                # Si el usuario no es el vendedor, actualiza el campo id_comprador
                registroTienda_data['id_comprador'] = request.session.get('username')
                registroTienda_serializer = RegistroTiendaSerializer(registroTienda, data=registroTienda_data, partial=True)

            #se guarda con la validacion
            if registroTienda_serializer.is_valid():
                registroTienda_serializer.save()
                return JsonResponse("Se Actualizo",safe=False)
            return JsonResponse("No se Actualizo",safe=False)
      
      
        #Elimiar registro de la tabla
        elif request.method=="DELETE":
            #Por medio del id se elimina
            registroTienda=RegistroTienda.objects.get(RegistroTiendaId=id)
            registroTienda.delete()
            return JsonResponse("Se Elimino",safe=False)
        return JsonResponse("No se Elimino",safe=False)
    else:
    # El usuario no está autenticado, redirige a la página de inicio
        return HttpResponseRedirect('/ruta-vista-en-angular/')  # Cambia la ruta




#para el cambio del estado de envio y recibido se crea nuevas vistas 
""" 
# ...

@csrf_exempt
def cambiar_estado_envio(request, id=0):
    # Verifica si el usuario está autenticado
    if request.session.get('is_authenticated'):
        if request.method == 'PUT':
            try:
                registroTienda = RegistroTienda.objects.get(RegistroTiendaId=id)
            except RegistroTienda.DoesNotExist:
                return HttpResponseNotFound("El registro no existe", status=404)

            # Verifica si el usuario que realiza la solicitud es el vendedor
            if registroTienda.id_vendedor == request.session.get('username'):
                # Cambia el estado de envío a True
                registroTienda.estado_envio = True
                registroTienda.save()
                return JsonResponse("Estado de envío cambiado a True", safe=False)
            else:
                return HttpResponseBadRequest("No tiene permiso para cambiar el estado de envío", status=400)
        else:
            return HttpResponseBadRequest("Método no permitido", status=400)
    else:
        return HttpResponseBadRequest("Usuario no autenticado", status=401)

@csrf_exempt
def cambiar_estado_recibido(request, id=0):
    # Verifica si el usuario está autenticado
    if request.session.get('is_authenticated'):
        if request.method == 'PUT':
            try:
                registroTienda = RegistroTienda.objects.get(RegistroTiendaId=id)
            except RegistroTienda.DoesNotExist:
                return HttpResponseNotFound("El registro no existe", status=404)

            # Verifica si el usuario que realiza la solicitud es el comprador
            if registroTienda.id_comprador == request.session.get('username'):
                # Cambia el estado recibido a True
                registroTienda.estado_recibido = True
                registroTienda.save()
                return JsonResponse("Estado recibido cambiado a True", safe=False)
            else:
                return HttpResponseBadRequest("No tiene permiso para cambiar el estado recibido", status=400)
        else:
            return HttpResponseBadRequest("Método no permitido", status=400)
    else:
        return HttpResponseBadRequest("Usuario no autenticado", status=401)
  """