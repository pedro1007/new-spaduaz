from django.test import TestCase
from apps.nivel.models import Bandera, Codificacion, Nivel, Oficio
from apps.docente.models import DatosPersonales, Estado, Municipio
from django.core.exceptions import ValidationError
from django.db import IntegrityError

class BanderaModelTest(TestCase):

    def test_agrega_bandera(self):
        bandera = Bandera.objects.create(
            clave = 'ES',
            nombre = 'Estancia Sabatica',
            id_categoria = 1
        )
        bandera_uno = Bandera.objects.first()

        self.assertEqual(bandera, bandera_uno)
        self.assertEqual(bandera_uno.clave, 'ES')
        self.assertEqual(str(bandera_uno), 'Estancia Sabatica')

    
    def test_bandera_clave_null(self):
        with self.assertRaises(IntegrityError):
            bandera = Bandera.objects.create(
                clave = None,
                nombre = 'Estancia Sabatica',
                id_categoria = 1
            )
            bandera.full_clean()
    
    def test_bandera_nombre_null(self):
        with self.assertRaises(IntegrityError):
            bandera = Bandera.objects.create(
                clave = 'ES',
                nombre = None,
                id_categoria = 1
            )
            bandera.full_clean()
    
    def test_bandera_id_categoria_null(self):
        with self.assertRaises(IntegrityError):
            bandera = Bandera.objects.create(
                clave = 'ES',
                nombre = 'Estancia Sabatica',
                id_categoria = None
            )
            bandera.full_clean()
    

    def test_clave_excede_limite_de_caracteres(self):
        bandera = Bandera.objects.create(
            clave = 'ESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSs',
            nombre = 'Estancia Sabatica',
            id_categoria = 3
        )
        with self.assertRaises(ValidationError):
            bandera.full_clean()
    
    def test_nombre_excede_limite_de_caracteres(self):
        bandera = Bandera.objects.create(
            clave = 'ES',
            nombre = 'Estancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia SabaticaEstancia Sabatica',
            id_categoria = 3
        )
        with self.assertRaises(ValidationError):
            bandera.full_clean()

    def test_agregar_bandera_categoria_no_existente(self):
        bandera = Bandera.objects.create(
            clave = 'ES',
            nombre = 'Estancia Sabatica',
            id_categoria = 3
        )
        with self.assertRaisesMessage(ValidationError, 'Valor \'3\' no es una opción válida.'):
            bandera.full_clean()

class CodificacionModelTest(TestCase):

    def test_agrega_codificacion(self):
        codificacion = Codificacion.objects.create(
            cod = '110',
            tipo_nivel = 'C',
            grupo_laboral = 'Prueba',
            categoria = 'Prueba Normal'
        )
        codificacion_uno = Codificacion.objects.first()

        self.assertEqual(codificacion, codificacion_uno)
        self.assertEqual(codificacion_uno.cod, 110)
        self.assertEqual(str(codificacion_uno), '[110] Prueba Normal Prueba C')

    
    def test_codificacion_cod_null(self):
        with self.assertRaises(IntegrityError):
            codificacion = Codificacion.objects.create(
                cod = None,
                tipo_nivel = 'C',
                grupo_laboral = 'Prueba',
                categoria = 'Prueba Normal'
            )
            codificacion.full_clean()
    
    def test_codificacion_tipo_nivel_null(self):
        with self.assertRaises(IntegrityError):
            codificacion = Codificacion.objects.create(
                cod = '110',
                tipo_nivel = None,
                grupo_laboral = 'Prueba',
                categoria = 'Prueba Normal'
            )
            codificacion.full_clean()

    def test_codificacion_grupo_laboral_null(self):
        with self.assertRaises(IntegrityError):
            codificacion = Codificacion.objects.create(
                cod = '110',
                tipo_nivel = 'Prueba',
                grupo_laboral = None,
                categoria = 'Prueba Normal'
            )
            codificacion.full_clean()

    def test_codificacion_categoria_null(self):
        with self.assertRaises(IntegrityError):
            codificacion = Codificacion.objects.create(
            cod = '110',
            tipo_nivel = 'C',
            grupo_laboral = 'Prueba',
            categoria = None
        )
            codificacion.full_clean()

    def test_cod_excede_limite_de_valor(self):
        codificacion = Codificacion.objects.create(
                cod = '110100',
                tipo_nivel = 'C',
                grupo_laboral = 'Prueba',
                categoria = 'Prueba Normal'
        )
        with self.assertRaises(ValidationError):
            codificacion.full_clean()

    def test_tipo_nivel_excede_limite_de_caracteres(self):
        codificacion = Codificacion.objects.create(
                cod = '110',
                tipo_nivel = 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCcc',
                grupo_laboral = 'Prueba',
                categoria = 'Prueba Normal'
        )
        with self.assertRaises(ValidationError):
            codificacion.full_clean()

    def test_grupo_laboral_excede_limite_de_caracteres(self):
        codificacion = Codificacion.objects.create(
                cod = '110',
                tipo_nivel = 'C',
                grupo_laboral = 'PruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPruebaPrueba',
                categoria = 'Prueba Normal'
        )
        with self.assertRaises(ValidationError):
            codificacion.full_clean()
    
    def test_categoria_excede_limite_de_caracteres(self):
        codificacion = Codificacion.objects.create(
                cod = '110',
                tipo_nivel = 'C',
                grupo_laboral = 'Prueba',
                categoria = 'Prueba NormalPrueba NormalPrueba NormalPrueba NormaPrueba Normall'
        )
        with self.assertRaises(ValidationError):
            codificacion.full_clean()

class NivelModelTest(TestCase):

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
        self.oficio = Oficio.objects.create(
            numero = 1231,
            emisor = 'COMISION MIXTA',
            fecha_oficio = '1997-12-09'
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

    def test_agrega_nivel(self):
        nivel = Nivel.objects.create(
            datos_personales = self.datos_personales,
            oficio = self.oficio,
            fecha_movimiento = '1997-12-09',
            via = 'REQUISITOS',
            bandera = self.bandera,
            cod_nivel = self.codificacion
        )
        nivel_uno = Nivel.objects.first()

        self.assertEqual(nivel, nivel_uno)
        self.assertEqual(nivel_uno.via, 'REQUISITOS')
        self.assertEqual(str(nivel_uno), 'José Andrés Muro Vargas Vía:REQUISITOS Bandera: Estancia Sabatica')
    
    def test_nivel_datos_personales_null(self):
        with self.assertRaises(IntegrityError):
            nivel = Nivel.objects.create(
                datos_personales = None,
                oficio = self.oficio,
                fecha_movimiento = '1997-12-09',
                via = 'REQUISITOS',
                bandera = self.bandera,
                cod_nivel = self.codificacion
            )
            nivel.full_clean()

    def test_nivel_oficio_null(self):
        with self.assertRaises(IntegrityError):
            nivel = Nivel.objects.create(
                datos_personales = self.datos_personales,
                oficio = None,
                fecha_movimiento = '1997-12-09',
                via = 'REQUISITOS',
                bandera = self.bandera,
                cod_nivel = self.codificacion
            )
            nivel.full_clean()

    def test_nivel_fecha_movimiento_null(self):
        with self.assertRaises(IntegrityError):
            nivel = Nivel.objects.create(
                datos_personales = self.datos_personales,
                oficio = self.oficio,
                fecha_movimiento = None,
                via = 'REQUISITOS',
                bandera = self.bandera,
                cod_nivel = self.codificacion
            )
            nivel.full_clean()

    def test_nivel_via_null(self):
        with self.assertRaises(IntegrityError):
            nivel = Nivel.objects.create(
                datos_personales = self.datos_personales,
                oficio = self.oficio,
                fecha_movimiento = '1997-12-09',
                via = None,
                bandera = self.bandera,
                cod_nivel = self.codificacion
            )
            nivel.full_clean()

    def test_nivel_bandera_null(self):
        with self.assertRaises(IntegrityError):
            nivel = Nivel.objects.create(
                datos_personales = self.datos_personales,
                oficio = self.oficio,
                fecha_movimiento = '1997-12-09',
                via = 'REQUISITOS',
                bandera = None,
                cod_nivel = self.codificacion
            )
            nivel.full_clean()

    def test_nivel_cod_nivel_null(self):
        with self.assertRaises(IntegrityError):
            nivel = Nivel.objects.create(
                datos_personales = self.datos_personales,
                oficio = self.oficio,
                fecha_movimiento = '1997-12-09',
                via = 'REQUISITOS',
                bandera = self.bandera,
                cod_nivel = None
            )
            nivel.full_clean()

    def test_categoria_fecha_movimiento_formato_incorrecto(self):
        with self.assertRaises(ValidationError):
            nivel = Nivel.objects.create(
                datos_personales = self.datos_personales,
                oficio = self.oficio,
                fecha_movimiento = '19912323',
                via = 'REQUISITOS',
                bandera = self.bandera,
                cod_nivel = self.codificacion
            )
            nivel.full_clean()

    def test_categoria_via_opcion_erronea(self):
        nivel = Nivel.objects.create(
            datos_personales = self.datos_personales,
            oficio = self.oficio,
            fecha_movimiento = '1991-11-23',
            via = 'PRUEBA',
            bandera = self.bandera,
            cod_nivel = self.codificacion
        )
        with self.assertRaises(ValidationError):
            nivel.full_clean()

class OficioModeloTest(TestCase):

    def test_agrega_oficio(self):
        oficio = Oficio.objects.create(
            numero = 123,
            emisor = 'COMISION MIXTA',
            fecha_oficio = '2006-12-12'
        )
        oficio_uno = Oficio.objects.first()

        self.assertEqual(oficio, oficio_uno)
        self.assertEqual(oficio_uno.numero, 123)
        self.assertEqual(str(oficio_uno), 'Oficio 123 Fecha: 2006-12-12')
    
    def test_oficio_numero_null(self):
        with self.assertRaises(IntegrityError):
            oficio = Oficio.objects.create(
                numero = None,
                emisor = 'COMISION MIXTA',
                fecha_oficio = '2006-12-12'
            )
            oficio.full_clean()
    
    def test_oficio_emisor_null(self):
        with self.assertRaises(IntegrityError):
            oficio = Oficio.objects.create(
                numero = 123,
                emisor = None,
                fecha_oficio = '2006-12-12'
            )
            oficio.full_clean()

    def test_oficio_fecha_null(self):
        with self.assertRaises(IntegrityError):
            oficio = Oficio.objects.create(
                numero = 123,
                emisor = 'COMISION MIXTA',
                fecha_oficio = None
            )
            oficio.full_clean()
    
    def test_oficio_fecha_formato_incorrecto(self):
        with self.assertRaises(ValidationError):
            oficio = Oficio.objects.create(
                numero = 123,
                emisor = 'COMISION MIXTA',
                fecha_oficio = '123332123'
            )
            oficio.full_clean()

    def test_oficio_emisor_opcion_erronea(self):
        oficio = Oficio.objects.create(
            numero = 123,
            emisor = 'COMISION',
            fecha_oficio = '2006-12-12'
        )
        with self.assertRaises(ValidationError):
            oficio.full_clean()