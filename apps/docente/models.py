import os
from uuid import uuid4
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.docente.choices import *

def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if isinstance (instance,GradosAcademicos):
        upload_to = 'grados_academicos'
        filename = '{}_{}_{}.{}'.format(instance.nombre_estudio, instance.docente,instance.fecha_obtencion, ext)
    elif isinstance (instance,DocenteIncidencia):
        upload_to = 'incidencias'
        filename = '{}_{}_{}.{}'.format(instance.categoria_incidencia, instance.docente,instance.fecha_inicio, ext)
    elif isinstance (instance, Interrupcion):
        upload_to = 'interrupciones'
        filename = 'Interrupcion_{}_{}.{}'.format(instance.docente,instance.fecha_inicio, ext)
    elif isinstance (instance, Prodep):
        upload_to = 'Prodep'
        filename = 'Prodep_{}_{}.{}'.format(instance.docente,instance.clave, ext)
    elif isinstance (instance, Sni):
        upload_to = 'Sni'
        filename = 'Sni_{}_{}.{}'.format(instance.docente,instance.clave, ext)
    else:
        upload_to = 'documentos'

    # return the whole path to the file
    return os.path.join(upload_to, filename)

# Create your models here.
LONGITUD_MAXIMA = 'Excediste la longitud'
class CategoriaIncidencias(models.Model):
    permiso = models.CharField(max_length=150)
    clausula = models.IntegerField(validators=[
            MaxValueValidator(1000),
            MinValueValidator(1)
        ])
    
    def __str__(self):
        return self.permiso

class CategoriaGrados(models.Model):
    nombre = models.CharField(max_length=20, choices=CATEGORIA_GRADOS)
    desc = models.TextField(max_length=150)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    id = models.CharField(primary_key=True,max_length=2)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    estado = models.ForeignKey(Estado, verbose_name="Estado", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 

class Escuela(models.Model):
    nombre = models.CharField(max_length=150)
    clave = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre}"

class UnidadAcademica(models.Model):
    clave_nueva = models.CharField(max_length=10)
    clave_antigua = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"

class Programa(models.Model):
    programa = models.CharField(max_length=100)
    unidad_academica = models.ForeignKey(UnidadAcademica, verbose_name="Unidad Académica", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.programa}"

class Materia(models.Model):
    nombre = models.CharField(max_length = 100)
    clave = models.CharField(max_length = 20)
    semestre = models.CharField(max_length = 50)
    programa = models.ForeignKey(Programa,verbose_name="Programa", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"

class CuerpoAcademico(models.Model):
    no_registro = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 100)
    unidad_academica = models.ForeignKey(UnidadAcademica, verbose_name="Unidad Académica", on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.nombre}"

class DatosPersonales(models.Model):
    nombres = models.CharField(max_length = 100)
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    rfc = models.CharField(max_length=13)
    curp = models.CharField(max_length=18)
    nss = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50, choices=SEXO)
    estado_civil = models.CharField(max_length=50, choices=ESTADO_CIVIL)
    domicilio = models.CharField(max_length=150)
    municipio = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)
    status = models.BooleanField(default=True,verbose_name="Estatus del Docente")

    def __str__(self):
        return f"{self.nombres} {self.ap_paterno} {self.ap_materno}"
    
class DatosLaborales(models.Model):
    datos_personales = models.OneToOneField(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    matricula_docente = models.CharField(max_length=4)
    matricula_nomina = models.CharField(max_length=6)
    fecha_ingreso = models.DateField()
    no_expediente = models.DecimalField(max_digits=6,decimal_places=2,null=True,max_length=20)
    exclusivo = models.BooleanField(verbose_name="Exclusivo de la UAZ")
    observaciones_exc = models.TextField(blank=True, null=True)
    cvu = models.CharField(blank=True, null=True,max_length=20)
    cuerpo_academico = models.ForeignKey(CuerpoAcademico, verbose_name="Cuerpo Academico", on_delete=models.CASCADE, blank=True, null=True)
    observaciones_c_a = models.TextField(blank=True, null=True)
    ##perfil = models.CharField(null=True,max_length=50)7t6
    programa = models.ManyToManyField(Programa)
    def __str__(self):
        return f"Datos laborales de {self.datos_personales}"

class GradosAcademicos(models.Model):
    docente = models.ForeignKey(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    escuela = models.ForeignKey(Escuela, verbose_name="Escuela", on_delete=models.CASCADE)
    fecha_obtencion = models.DateField()
    categoria_grados = models.CharField(max_length=15, choices=CATEGORIA_GRADOS)
    nombre_estudio = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, blank=True, null=True)
    imagen_grado = models.ImageField(verbose_name='Archivo de Grado Academico', upload_to=path_and_rename,blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_estudio} {self.docente}"

class DocenteIncidencia(models.Model):
    docente = models.ForeignKey(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    categoria_incidencia = models.ForeignKey(CategoriaIncidencias, verbose_name="Incidencia", on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    imagen_incidencia = models.ImageField(verbose_name='Archivo de incidencia', upload_to=path_and_rename)

    def __str__(self):
        return f"{self.categoria_incidencia} {self.docente} {self.fecha_inicio}-{self.fecha_fin}"

class Conacyt(models.Model):
    docente = models.ForeignKey(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    numero_proyecto = models.CharField(max_length=20, blank=True, null=True) 
    nombre_proyecto = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio_conacyt = models.DateField(blank=True, null=True)
    fecha_fin_conacyt = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre_proyecto

class Prodep(models.Model):
    docente = models.ForeignKey(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    clave = models.CharField(max_length=20, blank=True, null=True) 
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio_prodep = models.DateField(blank=True, null=True)
    fecha_fin_prodep = models.DateField(blank=True, null=True)
    imagen_prodep = models.ImageField(verbose_name='Archivo de Prodep', upload_to=path_and_rename, blank=True, null=True)

    
    def __str__(self):
        return self.descripcion

class Sni(models.Model):
    docente = models.ForeignKey(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    clave = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio_sni = models.DateField(blank=True, null=True)
    fecha_fin_sni = models.DateField(blank=True, null=True)
    nivel = models.CharField(max_length=50, choices=NIVELES_SNI, blank=True, null=True)
    imagen_sni = models.ImageField(verbose_name='Archivo de SNI', upload_to=path_and_rename,blank=True, null=True)

    def __str__(self):
        return self.descripcion

class Interrupcion(models.Model):
    docente = models.ForeignKey(DatosPersonales, verbose_name="Docente", on_delete=models.CASCADE)
    incidencias = models.ForeignKey(DocenteIncidencia, verbose_name="Incidencia", on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    imagen_interrupcion = models.ImageField(verbose_name='Archivo de Interrupcion', upload_to=path_and_rename)

    def __str__(self):
        return f"{self.docente} {self.fecha_inicio} {self.fecha_fin}"
