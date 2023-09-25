from rest_framework import serializers
from LoginAPP.models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuarios
        fields=('UsuariosId','UsuarioName','Password')
