from django.contrib import admin
from RegistroHoras.Actividades.models import Actividad

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'usuario' , 'fecha', )
    ordering = ['ticket',]



admin.site.register(Actividad, ActividadAdmin)


