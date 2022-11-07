from django import forms


class CursoFormulario(forms.Form):

    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    fecha_de_inicio = forms.DateField()
    
class EntregablesForm(forms.Form):

    tema = forms.CharField(max_length=30)
    fecha_de_entrega = forms.DateField()
    
class ProfesoresForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    catedra = forms.CharField(max_length=30)
    
class EstudiantesForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    comision = forms.CharField(max_length=30)
   
    
# forms de blogcoder

class ArticuloForm(forms.Form):

    titulo = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=1000)
    fecha = forms.DateField()
    

class AutorForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesion = forms.CharField(max_length=30)
    

class SeccionForm(forms.Form):

    nombre = forms.CharField(max_length=30)