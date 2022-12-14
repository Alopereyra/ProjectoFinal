from django.http import HttpResponse
from django.shortcuts import render

from blogcoder.models import Curso, Entregables, Articulos, Seccion, Autor, Profesores, Estudiantes
from blogcoder.forms import ArticuloForm, AutorForm, SeccionForm, EntregablesForm, ProfesoresForm, EstudiantesForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def procesar_formulario_entregable(request):
    if request.method != "POST":
        mi_entregable = EntregablesForm ()
    else:
        mi_entregable = EntregablesForm(request.POST)
        if mi_entregable.is_valid():
            informacion = mi_entregable.cleaned_data
            entregables = Entregables(tema=informacion["tema"], fecha_de_entrega=informacion["fecha_de_entrega"])
            entregables.save()
            return render(request, "blogcoder/inicio.html")
        
    contexto = {"formulario": mi_entregable}
    return render(request, "blogcoder/entregable.html", contexto)

def procesar_formulario_articulo(request):
    if request.method != "POST":
        mi_formulario = ArticuloForm()
    else:
        mi_formulario = ArticuloForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            articulo = Articulos(titulo=informacion["titulo"], texto=informacion["texto"],fecha=informacion["fecha"])
            articulo.save()
            return render(request, "blogcoder/inicio.html")
        
    contexto = {"formulario": mi_formulario}
    return render(request, "blogcoder/formulario-articulo.html", context=contexto)


def procesar_formulario_seccion(request):
    if request.method != "POST":
        mi_formulario = SeccionForm()
    else:
        mi_formulario = SeccionForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            seccion = Seccion(nombre=informacion["nombre"])
            seccion.save()
            return render(request, "blogcoder/inicio.html")
        
    contexto = {"formulario": mi_formulario}
    return render(request, "blogcoder/formulario-seccion.html", context=contexto)


def procesar_formulario_autor(request):
    if request.method != "POST":
        mi_formulario = AutorForm ()
    else:
        mi_formulario = AutorForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            seccion = Autor(nombre=informacion["nombre"], apellido=informacion["apellido"], profesion=informacion["profesion"])
            seccion.save()
            return render(request, "blogcoder/inicio.html")
        
    contexto = {"formulario": mi_formulario}
    return render(request, "blogcoder/formulario-seccion.html", contexto)


def ayuda(request):
    pass
    #return render(request, "blogcoder/ayuda.html")


def mostrar_inicio(request):
    return render(request, "blogcoder/inicio.html")


def cursos(request):
    return render(request, "blogcoder/cursos.html")


def profesores(request):
    if request.method != "POST":
        mi_formulario = ProfesoresForm ()
    else:
        mi_formulario = ProfesoresForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profes = Profesores(nombre=informacion["nombre"], catedra=informacion["catedra"])
            profes.save()
            return render(request, "inicio.html")
        
    contexto = {"formulario": mi_formulario}
    return render(request, "blogcoder/profesores.html", contexto)


def estudiantes(request):
    if request.method != "POST":
        mi_formulario = EstudiantesForm ()
    else:
        mi_formulario = EstudiantesForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            estudiantes = Estudiantes(nombre=informacion["nombre"], apellido=informacion["apellido"], comision=informacion["comision"])
            estudiantes.save()
            return render(request, "blogcoder/inicio.html")
        
    contexto = {"formulario": mi_formulario}
    return render(request, "blogcoder/estudiantes.html", contexto)


def entregables(request):
    return render(request, "blogcoder/entregables.html")


def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "blogcoder/formulario.html")

    curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"]) 
    curso.save()
    return render(request, "blogcoder/inicio.html")


def procesar_formulario_entregable(request):
    if request.method != "POST":
        mi_entregable = EntregablesForm ()
    else:
        mi_entregable = EntregablesForm(request.POST)
        if mi_entregable.is_valid():
            informacion = mi_entregable.cleaned_data
            entregables = Entregables(tema=informacion["tema"], fecha_de_entrega=informacion["fecha_de_entrega"])
            entregables.save()
            return render(request, "blogcoder/inicio.html")
        
    contexto = {"formulario": mi_entregable}
    
    return render(request, "blogcoder/formulario-entregable.html", contexto)


def busqueda(request):
    return render(request, "blogcoder/busqueda.html")

def buscar(request):
    respuesta = f"Buscando la camada nro: {request.GET['camada']}"
    return HttpResponse(respuesta)  # TODO: podr??amos mostrarla, no?


def busqueda_2(request):
    return render(request, "blogcoder/busqueda_2.html")

def buscar_2(request):

    if not request.GET["camada"]:
        return HttpResponse("No enviaste datos")
    else:
        camada_a_buscar = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada_a_buscar)
        
        contexto = {"camada": camada_a_buscar, 
                    "cursos_encontrados": cursos
                    }
        
        return render(request, "blogcoder/resultado_busqueda.html", contexto)
    
    
def busqueda_titulo(request):
    return render(request, "blogcoder/busqueda_titulo.html")

def buscar_titulo(request):

    if not request.GET["titulo"]:
        return HttpResponse("No enviaste datos")
    else:
        titulo_a_buscar = request.GET["titulo"]
        profe = Articulos.objects.filter(titulo=titulo_a_buscar)

        contexto = {"titulo": titulo_a_buscar,
                    "titulos_encontrados": profe
                    }

        return render(request, "blogcoder/resultado_busqueda_titulo.html", contexto)
    
    
    
def listar_cursos(request):
    todos_los_cursos = Curso.objects.all()
    
    contexto = {"cursos_encontrados": todos_los_cursos}
    
    return render(request, "blogcoder/listar-cursos.html", contexto)
     

def listar_articulos(request):
    pass  

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

class MyLogin(LoginView):
    template_name = "blogcoder/login.html"
    
class MyLogout(LogoutView):
    template_name = "blogcoder/logout.html"
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(request, "blogcoder/inicio.html", {"mensaje": f"Usuario: {username_capturado}"})

    else:
        form = UserCreationForm()

    return render(request, "blogcoder/registro.html", {"form": form})

@login_required
def mostrar_inicio(request):
    return render(request, "blogcoder/inicio.html")


class ArticulosList(ListView, LoginRequiredMixin):
    model = Articulos
    template_name = "blogcoder/articulos-lista.html"   
    
class ArticulosDetalle(DetailView, LoginRequiredMixin):
    model = Articulos
    template_name = "blogcoder/articulos_detalle.html" 
    
    
from django.urls import reverse
    
class ArticulosCreacion(CreateView, LoginRequiredMixin):
    model = Articulos
    fields = ["titulo", "texto", "fecha"]

    def get_success_url(self):
        return reverse("ArticulosList")


class ArticulosUpdateView(UpdateView, LoginRequiredMixin):
    model = Articulos
    success_url = "/blogcoder/articulos/list"
    fields = ["titulo", "texto", "fecha"]


class ArticulosDelete(DeleteView, LoginRequiredMixin):

    model = Articulos
    success_url = "/blogcoder/articulos/list"
    