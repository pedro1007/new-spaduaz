import os
from uuid import uuid4
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.docente.choices import *
from apps.docente.models import DatosPersonales


# Create your models here.
def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if isinstance (instance,Jubilado):
        upload_to = 'jubilados'
        filename = '{}_{}.{}'.format(instance.docente, instance.fecha, ext)
    elif isinstance (instance,Pensionado):
        upload_to = 'pensionados'
        filename = '{}_{}.{}'.format(instance.docente, instance.fecha, ext)
    elif isinstance (instance,Oficio):
        upload_to = 'oficios'
        filename = '{}_{}.{}'.format(instance.numero, instance.fecha_oficio, ext)
    else:
        upload_to = 'documentos'        

    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Codificacion(models.Model):
    cod = models.IntegerField(validators=[
            MaxValueValidator(999),
            MinValueValidator(1)
        ])
    tipo_nivel = models.CharField(max_length=10,choices=NIVEL)
    grupo_laboral = models.CharField(max_length=100,choices=GPO_LABORAL)
    categoria = models.CharField(max_length=50,choices=CATEGORIA_COD)

    def __str__(self):
        return f"[{self.cod}] {self.categoria} {self.grupo_laboral} {self.tipo_nivel}"

LONGITUD_MAXIMA = 'Excediste la longitud'
class Bandera(models.Model):
    clave = models.CharField(max_length=10, verbose_name="Clave")
    nombre = models.CharField(max_length=120)
    id_categoria = models.CharField(max_length=5, choices=CATEGORIAS_BANDERA)

    def __str__(self):
        return self.nombre
    
class Oficio(models.Model):
    numero = models.IntegerField()
    emisor = models.CharField(max_length=20, choices=OFICIO)
    fecha_oficio = models.DateField()
    imagen_oficios = models.ImageField("Oficio", upload_to=path_and_rename, null=True, blank=True)
    
    def __str__(self):
        return f"Oficio {self.numero} Fecha: {self.fecha_oficio}"

    
class Pensionado(models.Model):
    docente = models.ForeignKey(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    #bandera = models.ForeignKey(Bandera, verbose_name="Bandera", on_delete=models.CASCADE)
    beneficiarios = models.CharField(max_length=10)
    fecha = models.DateField()
    oficio = models.ForeignKey(Oficio, verbose_name="Oficio", on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    
class Jubilado(models.Model):
    docente = models.ForeignKey(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    bandera = models.ForeignKey(Bandera, verbose_name="Bandera", on_delete=models.CASCADE)
    fecha = models.DateField()
    oficio = models.ForeignKey(Oficio, verbose_name="Oficio", on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)

class Nivel(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    oficio = models.ForeignKey(Oficio, verbose_name="Oficio", on_delete=models.CASCADE)
    fecha_movimiento = models.DateField()
    via = models.CharField(max_length=10, choices=VIA, default='REQUISITOS')
    bandera = models.ForeignKey(Bandera, verbose_name="Bandera", on_delete=models.CASCADE)
    cod_nivel = models.ForeignKey(Codificacion, verbose_name="Codificacion", on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.datos_personales} Vía:{self.via} Bandera: {self.bandera}"