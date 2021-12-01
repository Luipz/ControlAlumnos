from django.db import models

from django.contrib import admin

class Alumno(models.Model):
    nombres  =   models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombres, self.apellidos, self.edad, self.genero

class Curso(models.Model):
    nombre = models.CharField(max_length=60)
    catedratico = models.CharField(max_length=40)
    
    alumnos = models.ManyToManyField(Alumno, through='Asignacion')

    def __str__(self):
        return self.nombre, self.catedratico

class Asignacion (models.Model):
    seccion = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Curso, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class AlumnoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)