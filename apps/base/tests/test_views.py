from django.test import TestCase
from django.urls import reverse
from apps.base.models import Base
from apps.docente.models import *
from apps.nivel.models import *


class BaseViewTest(TestCase):
    def setUp(self):
        estado = Estado.objects.create(
            nombre='Zacatecas'
        )
        municipio = Municipio.objects.create(
            estado=estado,
            nombre='Zacatecas'
        )
        self.datos_personales = DatosPersonales.objects.create(
            nombres='Pedro',
            ap_paterno='Sánchez',
            ap_materno='Hinostroza',
            fecha_nacimiento='1999-10-07',
            rfc='SAHP981007KF7',
            curp='SAHP981007HZSNND03',
            nss='3124',
            sexo='HOMBRE',
            estado_civil='SOLTERO',
            domicilio='Priv. Caleros 116',
            municipio=municipio,
            status=True
        )
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
        self.base = Base.objects.create(
            datos_personales=self.datos_personales,
            fecha_movimiento='2019-03-25',
            bandera=self.bandera,
            codificacion=self.codificacion,
            #materia='Materia',
            funcion='Funcion'
        )

    def test_template_lista_base(self):
        response = self.client.get('/base/listar')
        self.assertTemplateUsed(response, 'base_docente/lista_bases.html')

    def test_url_lista_base(self):
        response = self.client.get('/base/listar')
        self.assertEqual(response.status_code, 200)
    
    def test_nombre_url_lista_base(self):
        response = self.client.get(reverse('base:base_listar'))
        self.assertEqual(response.status_code, 200)
