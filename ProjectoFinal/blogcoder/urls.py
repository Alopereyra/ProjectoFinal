from django.contrib import admin
from django.urls import path, include

from blogcoder.views import mostrar_inicio, entregables, estudiantes, cursos, profesores, ayuda

#procesar_formulario, procesar_formulario_2, busqueda, busqueda_2, buscar, buscar_2


urlpatterns = [
    path("inicio/", mostrar_inicio, name="inicio"),
    path("entregables/", entregables, name="entregables"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("cursos/", cursos, name="mis_cursos"),
    path("profesores/", profesores, name="profesores"),
    path("ayuda/", ayuda),
    #path("formulario/", procesar_formulario, name="formulario"),
    #path("formulario-2/", procesar_formulario_2, name="formulario_2"),
    #path("busqueda/", busqueda, name="busqueda"),
    #path("busqueda-2/", busqueda_2, name="busqueda-2"),
    #path("buscar/", buscar),
    #path("buscar-2/", buscar_2),
    ]