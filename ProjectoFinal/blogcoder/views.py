from django.http import HttpResponse
from django.shortcuts import render

from blogcoder.models import Curso
from blogcoder.forms import ArticuloForm, AutorForm, SeccionForm

# Create your views here.

def procesar_formulario_articulo(request):
    mi_formulario = ArticuloForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "blogcoder/formulario-articulo.html", context=contexto)


def procesar_formulario_seccion(request):
    mi_formulario = SeccionForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "blogcoder/formulario-seccion.html", context=contexto)


def procesar_formulario_autor(request):
    mi_formulario = AutorForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "blogcoder/formulario-autor.html", context=contexto)


def ayuda(request):
    pass
    #return render(request, "blogcoder/ayuda.html")


def mostrar_inicio(request):
    return render(request, "blogcoder/inicio.html")

def cursos(request):
    return render(request, "blogcoder/cursos.html")


def profesores(request):
    return render(request, "blogcoder/profesores.html")


def estudiantes(request):
    return render(request, "blogcoder/estudiantes.html")


def entregables(request):
    return render(request, "blogcoder/entregables.html")

def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "blogcoder/formulario.html")

    curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"]) 
    curso.save()
    return render(request, "blogcoder/inicio.html")

def busqueda(request):
    return render(request, "blogcoder/busqueda.html")

def buscar(request):
    respuesta = f"Buscando la camada nro: {request.GET['camada']}"
    return HttpResponse(respuesta)  # TODO: podríamos mostrarla, no?

def busqueda_2(request):
    return render(request, "blogcoder/busqueda_2.html")

def buscar_2(request):

    if not request.GET["camada"]:
        return HttpResponse("No enviaste datos")
    else:
        camada_a_buscar = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada_a_buscar)

        contexto = {"camada": camada_a_buscar, "cursos_encontrados": cursos}

        return render(request, "blogcoder/resultado_busqueda.html", contexto)
