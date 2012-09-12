from django.db import models

class Empleado(models.Model):
	Nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Empleado")
	ApellidoPaterno = models.CharField(max_length=100, unique=True, verbose_name="Apellido Paterno")
	ApellidoMaterno= models.CharField(max_length=100, unique=True, verbose_name="Apellido Materno")

	def  __unicode__(self):
		return self.ApellidoPaterno
	class Meta():
		ordering = ['ApellidoPaterno']


