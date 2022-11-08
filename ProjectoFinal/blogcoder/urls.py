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
    procesar_formulario_entregable,
    busqueda_titulo,
    buscar_titulo,
    listar_cursos,
    listar_articulos,
    ArticulosList,
    ArticulosDetalle,
    ArticulosCreacion,
    ArticulosUpdateView,
    ArticulosDelete,
    MyLogin,
    MyLogout,
    register,
       
            
    )


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
    path("formulario-entregable/", procesar_formulario_entregable, name="formulario_entregable"),
    path("busqueda/", busqueda, name="busqueda"),
    path("busqueda-2/", busqueda_2, name="busqueda-2"),
    path("buscar/", buscar),
    path("buscar-2/", buscar_2),
    path("busqueda-titulo/", busqueda_titulo, name="busqueda-titulo"),
    path("buscar-titulo/", buscar_titulo, name="buscar-titulo"),
    path("cursos-lista/", listar_cursos),
    path("articulos-lista/", listar_articulos),
    
    path("articulos/list", ArticulosList.as_view(), name="ArticulosList"),
    path("r'(?P<pk>\d+)^$'", ArticulosDetalle.as_view(), name="ArticulosDetail"),
    path("articulos-nuevo/'", ArticulosCreacion.as_view(), name="ArticulosNew"),
    path("r'editar/(?P<pk>\d+)^$'", ArticulosUpdateView.as_view(), name="ArticulosUpdate"),
    path("r'borrar/(?P<pk>\d+)^$'", ArticulosDelete.as_view(), name="ArticulosDelete"),
    
    #path("inicio/", mostrar_inicio, name="Inicio"),
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    #path("login2/", login_request, name="Login2"),  # Propuesta en las Slides
    path("register/", register, name="Register")
    
    ]