from django.shortcuts import render


# Importar HTTPResponse
from django.http import HttpResponse


# las vistas son funciones


# cliente -> pide -> request
# Servidor -> Responde -> Response
def bienvenida(request):
    # Responder
    return HttpResponse("Bienvenido")


def despedida(request):
    return HttpResponse("Despedida")


def saludo(request):
    return HttpResponse("Saludo a Koders")


def saludar_con_nombre(request, nombre):
    print("imprimiendo --->", nombre)
    return HttpResponse(f"hola {nombre}")


def bienvenida_mentor_o_koder(request, type):
    if type == "mentor":
        mensaje = "Hello mentor, here are your classes"
    elif type == "koder":
        mensaje = "Hello koder, welcome to Kodemia"
    else:
        mensaje = "You are not welcome here"

    return HttpResponse(mensaje)
