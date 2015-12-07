from django.contrib import admin

from escuela.models import Estudiante
from escuela.models import Tutor
from escuela.models import Profesor
from escuela.models import Departamento
from escuela.models import Curso
from escuela.models import Alumno_curso

#create your models display here
class ProfesorAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,          {'fields': ['nombre']}),
    #    ('Apellidos',   {'fields': ['apPaterno']}),
    #]
    #para mostrar solo algunos campos al editar o agregar
    #fields = ['nombre', 'apPaterno']

    #para mostrar por columnas
    list_display = ('cedula', 'nombre', 'apPaterno', 'apMaterno')

    #para agregar un filtro y mostrar solo los deseados
    list_filter = ['cedula']
    #para agregar una barra de busqueda
    search_fields = ['cedula']

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Tutor)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Departamento)
admin.site.register(Curso)
admin.site.register(Alumno_curso)
