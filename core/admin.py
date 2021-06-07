from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao') # Quando eu listar os eventos, ele irá mostrar o titulo a data do evento e a de criacao
    list_filter = ('usuario', 'data_evento',)

admin.site.register(Evento, EventoAdmin)
