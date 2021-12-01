from django.shortcuts import render

from django.contrib import messages
from .forms import CursoForm
from cursos.models import Curso, Asignacion

def curso_nueva(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            curso = Curso.objects.create(nombre=formulario.cleaned_data['nombre'], catedratico = formulario.cleaned_data['catedratico'])
            for alumno_id in request.POST.getlist('alumnos'):
                asignacion = Asignacion(alumno_id = alumno_id, curso_id = curso.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Curso Guardada Exitosamente')
    else:
        formulario = CursoForm()
    return render(request, 'curso/curso_editar.html', {'formulario': formulario})
