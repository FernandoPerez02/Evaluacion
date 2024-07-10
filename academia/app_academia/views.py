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
    return redirect('tabla')
    
""" Calificacion """
def califi(request):
    listcali = models.Calificacion.objects.all()
    return render(request, 'app_moduls/Calificacion/lista.html', {'listcali': listcali})

def agregarcal(request):
    data = {
        'form': forms.CalificacionForm()
    }
    
    if request.method == 'POST':
        formulario = forms.CalificacionForm(request.POST)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Registro Exitoso'
            
        else:
            data['mensaje'] = 'Registro fallido'
        
    return render(request, 'app_moduls/Calificacion/agregar.html', data)

def editarcal(request, id_calificacion):
    registro = get_object_or_404(models.Calificacion, id_calificacion = id_calificacion)
    
    data = {
        'form': forms.CalificacionForm(instance=registro)
    }
    
    if request.method == 'POST':
        formulario = forms.CalificacionForm(request.POST, instance=registro)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edicion Exitosa'
            
        else:
            data['mensaje'] = 'Edicion fallida'
    return render(request, 'app_moduls/Calificacion/editar.html', data)

def eliminarcal(request, id_calificacion):
    registro = get_object_or_404(models.Calificacion, id_calificacion = id_calificacion)
    registro.delete()
    
    
""" Cursos """
def listacur(request):
    listaest = models.Estudiante.objects.all()
    return render(request, 'liscur.html', {'listcur': listaest})

def agrecur(request):
    data = {
        'form': forms.CursoForm()
    }
    
    if request.method == 'POST':
        formulario = forms.CursoForm(request.POST)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Registro Exitoso'
            
        else:
            data['mensaje'] = 'Registro fallido'
        
    return render(request, 'app_moduls/curso/agregar.html', data)

def editar(request, id_curso):
    registro = get_object_or_404(models.Curso, id_curso = id_curso)
    
    data = {
        'form': forms.CursoForm(instance=registro)
    }
    
    if request.method == 'POST':
        formulario = forms.CursoForm(request.POST, instance=registro)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edicion Exitosa'
            
        else:
            data['mensaje'] = 'Edicion fallida'
    return render(request, 'app_moduls/curso/editar.html', data)

def eliminar(request, id_curso):
    registro = get_object_or_404(models.Curso, id_curso = id_curso)
    registro.delete()
    return redirect('curso')