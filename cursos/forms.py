from django import forms
from .models import Curso, Alumno


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'catedratico', 'alumnos')

    def __init__ (self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields["alumnos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["alumnos"].help_text = "Ingrese los Alumnos que asignarion este curso"
        self.fields["alumnos"].queryset = Alumno.objects.all()