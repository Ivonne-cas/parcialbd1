from django.contrib import admin
from apps.mantenimientos.models import Mantenimiento,MantenimientoEquipo
# Register your models here.
class MembershipInline (admin.TabularInline):
    model = MantenimientoEquipo
    extra = 1

class MantenimientoAdmin (admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display =('fecha','solicitud','tiempo')
    ordering =('fecha','solicitud','tiempo')
    search_fields =('fecha','solicitud')

admin.site.register (Mantenimiento,MantenimientoAdmin)