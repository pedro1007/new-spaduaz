from django.db import IntegrityError
from django.test import TestCase
from apps.base.forms import BaseForm
from apps.base.models import Base
from apps.docente.models import *
from apps.nivel.models import *


class BaseFormTest(TestCase):
    def setUp(self, datos_personales='', fecha_movimiento='', bandera='', codificacion='', materia='', funcion=''):
        self.data = {
            'datos_personales': datos_personales,
            'fecha_movimiento': fecha_movimiento,
            'bandera': bandera,
            'codificacion': codificacion,
            'materia': materia,
            'funcion': funcion
        }
        self.bandera = Bandera.objects.create(
            clave='AS',
            nombre='Año Sabático',
            id_categoria='BASE',
        )
        self.codificacion = Codificacion.objects.create(
            cod=1,
            tipo_nivel='ASOCIADO A',
            grupo_laboral='DOCENTE INVESTIGADOR',
            categoria='TIEMPO COMPLETO'
        )
        self.unidad_academica = UnidadAcademica.objects.create(
            clave_nueva=25262,
            clave_antigua=54545,
            nombre='Ingeniería Eléctrica'
        )
        self.programa = Programa.objects.create(
            programa='Ingeniería de Software',
            unidad_academica=self.unidad_academica
        )
        self.materia = Materia.objects.create(
            nombre='Estructuras de datos',
            clave='123',
            semestre=7,
            programa=self.programa
        )

    def test_si_el_formulario_es_invalido(self):
        self.data['datos_personales'] = '132131313121321322188'
        self.data['fecha_movimiento'] = '1321313131213213221'
        self.data['bandera'] = '9809080808'
        self.data['codificacion'] = '9809080808'
        self.data['materia'] = '9809080808'
        self.data['funcion'] = '9809080808'
        form = BaseForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_base_datos_personales_null(self):
        with self.assertRaises(IntegrityError):
            base = Base.objects.create(
                datos_personales = None,
                fecha_movimiento = '2006-12-12',
                bandera = self.bandera,
                codificacion = self.codificacion
            )
            base.full_clean()

   