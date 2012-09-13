from django.contrib import admin
from RegistroHoras.Actividades.models import Actividad

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'usuario' , 'fecha', )
    ordering = ['ticket',]

    class Media:
			js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/textarea.js')



admin.site.register(Actividad, ActividadAdmin)


