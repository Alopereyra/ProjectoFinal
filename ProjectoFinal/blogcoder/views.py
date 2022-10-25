from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

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

    # curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
    # curso.save()
    # return render(request, "blogcoder/inicio.html")
