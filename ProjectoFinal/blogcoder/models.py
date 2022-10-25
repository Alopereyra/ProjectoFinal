from pyexpat import model
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()
    fecha_de_inicio = models.DateField(null=True)

    def __str__(self):
        return f"({self.camada}) {self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    

class Autor(models.Model):
    
    class Meta:
        verbose_name_plural = "Autores"
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}"
    
class Articulos(models.Model):
    
    class Meta:
        verbose_name_plural = "Articulos"
    
    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null = True)
    
    def __str__(self) -> str:
        return f"{self.titulo}"
    
class Seccion(models.Model):
    
    class Meta:
        verbose_name_plural = "Secciones"
    
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre}"
    
    
    
