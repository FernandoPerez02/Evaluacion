from django import forms
from . import models

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = '__all__'