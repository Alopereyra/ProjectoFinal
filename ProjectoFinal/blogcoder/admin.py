from django.contrib import admin
from.models import Autor, Articulos, Curso, Entregables, Estudiantes, Profesores, Seccion 

# Register your models here.

admin.site.register(Curso)
admin.site.register(Estudiantes)
admin.site.register(Entregables)
admin.site.register(Profesores)


#blog
admin.site.register(Articulos)
admin.site.register(Autor)
admin.site.register(Seccion)
