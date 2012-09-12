from django.contrib import admin
from RegistroHoras.Empleados.models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'ApellidoPaterno', 'ApellidoMaterno',)
    ordering = ['ApellidoPaterno',]



admin.site.register(Empleado, EmpleadoAdmin)


