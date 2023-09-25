
from django.urls import re_path

from LoginAPP import views

urlpatterns=[
    re_path(r'^usuarios$',views.usuariosApi),
    re_path(r'^usuarios/([0-9]+)$',views.usuariosApi),

    # Otras rutas de tu aplicación
]