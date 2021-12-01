from django.contrib import admin

from cursos.models import Alumno, AlumnoAdmin, Curso, CursoAdmin

admin.site.register(Alumno, AlumnoAdmin)

admin.site.register(Curso, CursoAdmin)