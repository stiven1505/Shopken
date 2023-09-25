from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #Permite a otros dominio acceder a los metodos
from rest_framework.parsers import JSONParser #Analizar los datos JSON
from django.http.response import JsonResponse #Respuestas de datos JSON

from LoginAPP.models import Usuarios
from LoginAPP.serializers import UsuariosSerializer

#session
from django.contrib.sessions.models import Session


# Create your views here.

from django.contrib.auth import authenticate, login, logout

@csrf_exempt
def loginApi(request):
    if request.method == 'POST':
        # Obtener las credenciales del cliente desde los datos JSON
        data = JSONParser().parse(request)
        username = data.get('UsuarioName')
        password = data.get('Password')

        # Verificar las credenciales con la base de datos
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Las credenciales son válidas, iniciar sesión
            login(request, user)
            request.session['is_authenticated'] = True
            request.session['username'] = user.username  # Guarda el nombre de usuario
            return JsonResponse({"message": "Inicio de sesión exitoso"})
        else:
            request.session['is_authenticated'] = False
            # Las credenciales no son válidas, devolver un mensaje de error
            return JsonResponse({"message": "Nombre de usuario o contraseña incorrectos"}, status=401)


