from django.test import TestCase

from apps.docente.models import *
from apps.nivel.forms import *
from apps.nivel.models import *


class BanderaFormTest(TestCase):
    def setUp(self, clave='', nombre='', id_categoria=''):
        self.data = {
            'clave': clave,
            'nombre': nombre,
            'id_categoria': id_categoria,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['clave'] = '132131313121321322188'
        self.data['nombre'] = '1321313131213213221'
        self.data['id_categoria'] = '9809080808'
        form = BanderaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_max_length_nombre_bandera(self):
        self.data['nombre'] = 'Bandera jrfijlmcdslv,dl,amskcn jbxqfwdtyefwyvhklfbmvdfmvdbcbhasghjgvkjdankvacsajkbchjasvhjbdvjkuefehuehuiehguhweughuewvwgw'
        form = BanderaForm(
            self.data
        )
        self.assertEquals(form.errors['nombre'], [LONGITUD_MAXIMA])

    def test_bandera_nombre_vacio(self):
        bandera = Bandera.objects.create(
            clave='26161',
            id_categoria='5151'
        )
        form = BanderaForm(
            data={
                'nombre': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_bandera_clave_vacio(self):
        bandera = Bandera.objects.create(
            nombre='Bandera',
            id_categoria='5151'
        )
        form = BanderaForm(
            data={
                'clave': '',
            }
        )
        self.assertFalse(form.is_valid())

class CodificacionFormTest(TestCase):
    def setUp(self, cod='', tipo_nivel='', grupo_laboral='', categoria=''):
        self.data = {
            'Cod': cod,
            'tipo_nivel': tipo_nivel,
            'grupo_laboral': grupo_laboral,
            'categoria': categoria,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['cod'] = '132131313121321322188'
        self.data['tipo_nivel'] = '1321313131213213221'
        self.data['grupo_laboral'] = '1321313131213213221'
        self.data['categoria'] = '98090808087686787878786787686'
        form = BanderaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_codificacion_tipo_nivel_vacio(self):
        cod = Codificacion.objects.create(
            cod='26161',
            grupo_laboral='Docente Investigador',
            categoria='Tiempo Completo'
        )
        form = CodificacionForm(
            data={
                'tipo_nivel': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_codificacion_grupo_laboral_vacio(self):
        cod = Codificacion.objects.create(
            cod='26161',
            tipo_nivel='Titular A',
            categoria='Tiempo Completo'
        )
        form = CodificacionForm(
            data={
                'grupo_laboral': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_codificacion_categoria_vacio(self):
        cod = Codificacion.objects.create(
            cod='26161',
            tipo_nivel='45155',
            grupo_laboral='Docente Investigador'
        )
        form = CodificacionForm(
            data={
                'categoria': '',
            }
        )
        self.assertFalse(form.is_valid())

class OficioFormTest(TestCase):
    def setUp(self, numero='', emisor='', fecha_oficio='', imagen_oficio=''):
        self.data = {
            'numero': numero,
            'emisor': emisor,
            'fecha_oficio': fecha_oficio,
            'imagen_oficios': imagen_oficio,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['numero'] = 'numerososososos'
        self.data['emisor'] = '1321313131213213221'
        self.data['fecha_oficio'] = '1321313131213213221'
        self.data['imagen_oficios'] = '98090808087686787878786787686'
        form = BanderaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_oficio_emisor_vacio(self):
        oficio = Oficio.objects.create(
            numero=1515,
            fecha_oficio='2018-12-14',
            imagen_oficios='D:\\Pictures\\pikachu.jpg'
        )
        form = OficioForm(
            data={
                'emisor': '',
            }
        )
        self.assertFalse(form.is_valid())

class NivelFormTest(TestCase):
    def setUp(self, datos_personales='', oficio='', fecha_movimiento='', via='', bandera='', cod_nivel='', observaciones=''):
        self.data = {
            'datos_personales': datos_personales,
            'oficio': oficio,
            'fecha_movimiento': fecha_movimiento,
            'via': via,
            'bandera': bandera,
            'cod_nivel': cod_nivel,
            'observaciones': observaciones,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['datos_personales'] = '132131313121321322188'
        self.data['oficio'] = '132131'
        self.data['fecha_movimiento'] = '132131'
        self.data['via'] = '9809'
        self.data['bandera'] = '9809'
        self.data['cod_nivel'] = '9809'
        self.data['observaciones'] = '980908'
        form = NivelForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_nivel_via_vacio(self):
        estado = Estado.objects.create(
            nombre='Zacatecas'
        )
        municipio = Municipio.objects.create(
            estado=estado,
            nombre='Guadalupe'
        )
        datos_personales = DatosPersonales.objects.create(
            nombres='Viridiana',
            ap_paterno='Gutiérrez',
            ap_materno='Villalobos',
            fecha_nacimiento='1997-02-11',
            rfc='GUVM970211HU7',
            curp='GUVM970211MSTLT09',
            nss='4834',
            domicilio='Jose Ma. Coss #26',
            municipio=municipio,
            status=True
        )
        bandera = Bandera.objects.create(
            nombre='Bandera',
            clave='26161',
            id_categoria='5151'
        )
        oficio = Oficio.objects.create(
            numero=1515,
            emisor='Rector',
            fecha_oficio='2018-12-14',
            imagen_oficios='D:\\Pictures\\pikachu.jpg'
        )
        cod = Codificacion.objects.create(
            cod='26161',
            tipo_nivel='Titular A',
            grupo_laboral='Docente Investigador',
            categoria='Tiempo Completo'
        )
        nivel = Nivel.objects.create(
            datos_personales=datos_personales,
            oficio=oficio,
            fecha_movimiento='2019-04-25',
            bandera=bandera,
            cod_nivel=cod,
            observaciones='Aquí va la observación'
        )
        form = NivelForm(
            data={
                'via': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_nivel_bandera_vacio(self):
        estado = Estado.objects.create(
            nombre='Zacatecas'
        )
        municipio = Municipio.objects.create(
            estado=estado,
            nombre='Guadalupe'
        )
        datos_personales = DatosPersonales.objects.create(
            nombres='Viridiana',
            ap_paterno='Gutiérrez',
            ap_materno='Villalobos',
            fecha_nacimiento='1997-02-11',
            rfc='GUVM970211HU7',
            curp='GUVM970211MSTLT09',
            nss='4834',
            domicilio='Jose Ma. Coss #26',
            municipio=municipio,
            status=True
        )
        bandera = Bandera.objects.create(
            nombre='Bandera',
            clave='26161',
            id_categoria='5151'
        )
        oficio = Oficio.objects.create(
            numero=1515,
            emisor='Rector',
            fecha_oficio='2018-12-14',
            imagen_oficios='D:\\Pictures\\pikachu.jpg'
        )
        cod = Codificacion.objects.create(
            cod='26161',
            tipo_nivel='Titular A',
            grupo_laboral='Docente Investigador',
            categoria='Tiempo Completo'
        )
        nivel = Nivel.objects.create(
            datos_personales=datos_personales,
            oficio=oficio,
            fecha_movimiento='2019-04-25',
            via='Requisitos',
            bandera=bandera,
            cod_nivel=cod,
            observaciones='Aquí va la observación'
        )
        form = NivelForm(
            data={
                'bandera': None,
            }
        )
        self.assertFalse(form.is_valid())