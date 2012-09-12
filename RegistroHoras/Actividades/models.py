from django.db import models
from django.contrib.auth.models import User


class Actividad(models.Model):
	ticket = models.CharField(max_length=100, unique=True, verbose_name="No. Ticket")
	usuario = models.ForeignKey(User, verbose_name="Nombre de Empleado")
	fecha = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Fecha de la Actividad")

	def  __unicode__(self):
		return self.ticket
		