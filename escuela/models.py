from django.db import models

# Create your models here.
class Tutor(models.Model):
    nombre = models.CharField(max_length = 20)
    apPaterno = models.CharField(max_length = 20)
    apMaterno = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 7)
    celular = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.nombre+' '+self.apPaterno+' '+self.apMaterno

class Estudiante(models.Model):
    nombre = models.CharField(max_length = 20)
    apPaterno = models.CharField(max_length = 20)
    apMaterno = models.CharField(max_length = 20)
    calificacion = models.IntegerField(default=0)
    tutor = models.ForeignKey(Tutor)

    def __unicode__(self):
        return self.apPaterno+' '+self.apMaterno+' '+self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length = 20)
    apPaterno = models.CharField(max_length = 20)
    apMaterno = models.CharField(max_length = 20)
    cedula = models.CharField(max_length = 20, primary_key = True)
    telefono = models.CharField(max_length = 7)
    direccion = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.nombre + ' ' + self.apPaterno + ' ' + self.apMaterno + ' ' +self.email

class Departamento(models.Model):
    clave_dpto = models.CharField(max_length = 10, primary_key = True)
    nombre_dpto = models.CharField(max_length = 20)

class Curso(models.Model):
    cedula_profesor = models.ForeignKey(Profesor)
    clave_dpto = models.ForeignKey(Departamento)
    seccion = models.IntegerField(default=0)
    grado_curso = models.IntegerField(default=0)

class Alumno_curso(models.Model):
    id_estudiante = models.ForeignKey(Estudiante)
    clave_curso = models.ForeignKey(Curso)
    cedula_profesor = models.ForeignKey(Profesor)
