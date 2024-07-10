from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from . import forms

# Create your views here.
def base(request):
    return render(request, 'base.html')

def tabla(request):
    listaest = models.Estudiante.objects.all()
    return render(request, 'tabla.html', {'listaest': listaest})

def nuevoestu(request):
    data = {
        'form': forms.EstudianteForm()
    }
    
    if request.method == 'POST':
        formulario = forms.EstudianteForm(request.POST)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Registro Exitoso'
            
        else:
            data['mensaje'] = 'Registro fallido'
        
    return render(request, 'datospersonals.html', data)

def editar(request, id_estudiante):
    registro = get_object_or_404(models.Estudiante, id_estudiante = id_estudiante)
    
    data = {
        'form': forms.EstudianteForm(instance=registro)
    }
    
    if request.method == 'POST':
        formulario = forms.EstudianteForm(request.POST, instance=registro)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edicion Exitosa'
            
        else:
            data['mensaje'] = 'Edicion fallida'
    return render(request, 'editar.html', data)

def eliminar(request, id_estudiante):
    registro = get_object_or_404(models.Estudiante, id_estudiante = id_estudiante)
    registro.delete()