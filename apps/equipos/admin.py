from django.contrib import admin
from django.db.models.base import Model
from apps.equipos.models import Equipo
# Register your models here.

class EquipoAdmin (admin.ModelAdmin):
    list_display =('nombre','marca','modelo')
    ordering =('nombre','marca','modelo')
    search_fields= ('nombre','marca')

admin.site.register(Equipo,EquipoAdmin)