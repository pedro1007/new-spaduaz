from django.db import models
from apps.docente.models import DatosPersonales, Materia
from apps.nivel.models import Oficio, Codificacion, Bandera

# Create your models here.
class Base(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    fecha_movimiento = models.DateField()
    bandera = models.ForeignKey(Bandera, verbose_name="Bandera", on_delete=models.CASCADE)
    codificacion = models.ForeignKey(Codificacion, verbose_name="Codificacion", on_delete=models.CASCADE)
    materia = models.ManyToManyField(Materia)
    funcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.datos_personales} {self.bandera}"