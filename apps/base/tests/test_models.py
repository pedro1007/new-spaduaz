from django.test import TestCase
from apps.docente.models import CategoriaGrados, DatosPersonales, Estado, Materia, Municipio, Programa, Programa, Programa, Programa, Programa, Programa, UnidadAcademica
from apps.nivel.models import Bandera, Codificacion
from apps.base.models import Base
from django.core.exceptions import ValidationError
from django.db import IntegrityError

class BaseModelTest(TestCase):
    def setUp(self):
        estado = Estado.objects.create(
            nombre = 'Zacatecas'
        )
        municipio = Municipio.objects.create(
            estado = estado,
            nombre = 'Guadalupe'
        )
        self.datos_personales = DatosPersonales.objects.create(
            nombres = 'José Andrés',
            ap_paterno = 'Muro',
            ap_materno = 'Vargas',
            fecha_nacimiento = '1997-12-09',
            rfc = 'MUVA971209GN1',
            curp = 'MUVA971209HZSRRN00',
            nss = '1234566',
            sexo = 'HOMBRE',
            estado_civil = 'SOLTERO',
            domicilio = 'Arroyo de la martinica #3 Indeco',
            municipio = municipio,
            status = True
        )
        self.bandera = Bandera.objects.create(
            clave = 'ES',
            nombre = 'Estancia Sabatica',
            id_categoria = 1
        )
        self.codificacion = Codificacion.objects.create(
            cod = '110',
            tipo_nivel = 'C',
            grupo_laboral = 'Prueba',
            categoria = 'Prueba Normal'
        )
        self.unidad_academica = UnidadAcademica.objects.create(
            clave_nueva = 111,
            clave_antigua = 11111,
            nombre = 'Ingenieria de Software'
        )
        self.programa = Programa.objects.create(
            programa = 'Ing. Software',
            unidad_academica = self.unidad_academica
        )

        self.materia = Materia.objects.create(
            nombre = 'Estructuras de datos',
            clave = '123',
            semestre = 7,
            programa = self.programa
        )

    def test_agrega_base(self):
            base = Base.objects.create(
                datos_personales = self.datos_personales,
                fecha_movimiento = '2006-12-12',
                bandera = self.bandera,
                codificacion = self.codificacion
            )
            base_uno = Base.objects.first()

            self.assertEqual(base, base_uno)
            self.assertEqual(str(base_uno), 'José Andrés Muro Vargas Estancia Sabatica')
    
    def test_base_datos_personales_null(self):
        with self.assertRaises(IntegrityError):
            base = Base.objects.create(
                datos_personales = None,
                fecha_movimiento = '2006-12-12',
                bandera = self.bandera,
                codificacion = self.codificacion
            )
            base.full_clean()

    def test_base_fecha_movimiento_null(self):
        with self.assertRaises(IntegrityError):
            base = Base.objects.create(
                datos_personales = self.datos_personales,
                fecha_movimiento = None,
                bandera = self.bandera,
                codificacion = self.codificacion
            )
            base.full_clean()

    def test_base_bandera_null(self):
        with self.assertRaises(IntegrityError):
            base = Base.objects.create(
                datos_personales = self.datos_personales,
                fecha_movimiento = '2006-12-12',
                bandera = None,
                codificacion = self.codificacion
            )
            base.full_clean()

    def test_base_codificacion_null(self):
        with self.assertRaises(IntegrityError):
            base = Base.objects.create(
                datos_personales = self.datos_personales,
                fecha_movimiento = '2006-12-12',
                bandera = self.bandera,
                codificacion = None
            )
            base.full_clean()

    def test_base_fecha_movimiento_formato_incorrecto(self):
        with self.assertRaises(ValidationError):
            base = Base.objects.create(
                datos_personales = self.datos_personales,
                fecha_movimiento = '2006-1212',
                bandera = self.bandera,
                codificacion = None
            )
            base.full_clean()