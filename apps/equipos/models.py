from django.db import models

# Create your models here.
class Equipo (models.Model):
    nombre= models.CharField(max_length=50,verbose_name="nombre")
    marca=models.CharField(max_length=50,verbose_name="marca")
    modelo= models.IntegerField ( verbose_name= "modelo")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name ="equipo"
        verbose_name_plural ="equipos"