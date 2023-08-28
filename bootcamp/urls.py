from django.contrib import admin
from django.urls import path

# Views se agrega cada una de las def de views...!
from .views import get_koder, list_koder
urlpatterns = [
    # Custom URLs
    path("koders/", list_koder),
    path("koder/id", get_koder),

]
