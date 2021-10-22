from django.db import models
from apps.equipos.models import Equipo
# Create your models here.
class Mantenimiento (models.Model):
    fecha = models.DateField(verbose_name="fecha")
    solicitud =models.IntegerField(verbose_name="solicitud")
    tiempo = models.IntegerField(verbose_name="tiempo")
    equipo =models.ManyToManyField(Equipo,through="MantenimientoEquipo")

    def __str__(self):
        return self.fecha

    class Meta:
        verbose_name ="mantenimiento"
        verbose_name_plural ="mantenimientos"

class MantenimientoEquipo(models.Model):
    equipo =models.ForeignKey (Equipo,on_delete=models.CASCADE,verbose_name="equipo")
    mantenimiento =models.ForeignKey (Mantenimiento,on_delete=models.CASCADE,verbose_name="mantenimiento")
    descripcion =models.CharField(max_length=50,verbose_name="descripcion")
    resultado =models.BooleanField (verbose_name="resultado")