from django.db import models

# Create your models here.

class Usuarios(models.Model):
    UsuariosId = models.AutoField(primary_key=True)
    UsuarioName= models.CharField(max_length=500)
    Password=models.CharField(max_length=500)


    