from django.contrib import admin
from django.urls import path, include

from blogcoder.views import (
    mostrar_inicio, 
    entregables, 
    estudiantes, 
    cursos, 
    profesores, 
    ayuda, 
    procesar_formulario,
    busqueda, buscar, busqueda_2, buscar_2,
    procesar_formulario_articulo,
    procesar_formulario_seccion,
    procesar_formulario_autor,
        
    )

#  procesar_formulario_2


urlpatterns = [
    path("inicio/", mostrar_inicio, name="inicio"),
    path("formulario-articulo/", procesar_formulario_articulo, name="formulario_articulo"),
    path("formulario-seccion/", procesar_formulario_seccion, name="formulario_seccion"),
    path("formulario-autor/", procesar_formulario_autor, name="formulario_autor"),
    path("entregables/", entregables, name="entregables"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("cursos/", cursos, name="mis_cursos"),
    path("profesores/", profesores, name="profesores"),
    path("ayuda/", ayuda),
    path("formulario/", procesar_formulario, name="formulario"),
    
    path("busqueda/", busqueda, name="busqueda"),
    path("busqueda-2/", busqueda_2, name="busqueda-2"),
    path("buscar/", buscar),
    path("buscar-2/", buscar_2),
    ]