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

class Materia(models.Model):
    nombre_materia = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.nombre_materia

class Estudiante(models.Model):
    nombre = models.CharField(max_length = 20)
    apPaterno = models.CharField(max_length = 20)
    apMaterno = models.CharField(max_length = 20)
    tutor = models.ForeignKey(Tutor)
    grado = models.IntegerField(blank=True)

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

class Calificaciones(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    materia1 = models.ForeignKey(Materia, related_name='materia_materia1')
    calif1 = models.DecimalField(max_digits = 3, decimal_places = 1, default=0.0)
    materia2 = models.ForeignKey(Materia, related_name='materia_materia2')
    calif2 = models.DecimalField(max_digits = 3, decimal_places = 1, default=0.0)
    materia3 = models.ForeignKey(Materia, related_name='materia_materia3')
    calif3 = models.DecimalField(max_digits = 3, decimal_places = 1, default=0.0)
    materia4 = models.ForeignKey(Materia, related_name='materia_materia4')
    calif4 = models.DecimalField(max_digits = 3, decimal_places = 1, default=0.0)
    materia5 = models.ForeignKey(Materia, related_name='materia_materia5')
    calif5 = models.DecimalField(max_digits = 3, decimal_places = 1, default=0.0)
    materia6 = models.ForeignKey(Materia, related_name='materia_materia6')
    calif6 = models.DecimalField(max_digits = 3, decimal_places = 1, default=0.0)
    promedio = models.DecimalField(max_digits = 3, decimal_places = 1, default=0.0)
    promovido = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.estudiante)# + ' ' + str(self.promedio)+ ' ' + str(self.promovido)
