from django import forms
from . import models

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = '__all__'
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = '__all__'
        
class CalificacionForm(forms.ModelForm):
    class Meta:
        model = models.Calificacion
        fields = '__all__'