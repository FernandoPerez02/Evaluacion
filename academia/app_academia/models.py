from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    documento = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'estudiante'
        
class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    calificacion = models.CharField(max_length=10)
    id_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso')

    class Meta:
        managed = False
        db_table = 'calificacion'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=50)
    id_estudiante = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='id_estudiante')

    class Meta:
        managed = False
        db_table = 'curso'