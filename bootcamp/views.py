from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_koder(request):
    return HttpResponse("List")


def list_koder(request):
    return HttpResponse("get")
