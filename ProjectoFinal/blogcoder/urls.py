from django.contrib import admin
from django.urls import path, include

from blogcoder.views import mostrar_inicio

urlpatterns = [
    path("inicio/", mostrar_inicio)
]