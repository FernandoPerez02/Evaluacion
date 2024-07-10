from django.urls import path
from . import views

urlpatterns = [
    path('calificar/', views.nuevoestu, name='agregarestu'),
    path('', views.base, name='base'),
    path('tabla/', views.tabla, name='tabla'),
    path('editar/<id_estudiante>', views.editar, name='editar'),
    path('eliminar/<id_estudiante>', views.eliminar, name='eliminar'),
    
    path('califi/', views.califi, name='califi')
]