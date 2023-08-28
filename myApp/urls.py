from django.contrib import admin
from django.urls import path

# Views se agrega cada una de las def de views...!
from .views import bienvenida, despedida, saludo, saludar_con_nombre, bienvenida_mentor_o_koder

urlpatterns = [
    # Custom URLs
    path("despedida/", despedida),
    path("", bienvenida),
    path("saludo/", saludo),
    path("saludo/<str:nombre>", saludar_con_nombre),
    path("kodemia/<str:type>/", bienvenida_mentor_o_koder),
]
