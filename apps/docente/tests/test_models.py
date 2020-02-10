from django.test import TestCase
from apps.docente.models import *
from apps.docente.choices import *
import datetime
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from decimal import Decimal, DecimalException, InvalidOperation


class CatGradosModelTest(TestCase):
    def test_agrega_cat_grado(self):
        cat_grado = CategoriaGrados.objects.create(
            nombre = 'Primaria',
            desc = 'Grado Primaria'
        )
        cat_grado_uno = CategoriaGrados.objects.first()

        self.assertEqual(cat_grado, cat_grado_uno)
        self.assertEqual(cat_grado_uno.nombre, 'Primaria')
        self.assertEqual(str(cat_grado_uno), 'Primaria')

    def test_nombre_excede_limite_caracteres(self):
        cat_grado = CategoriaGrados.objects.create(
            nombre = 'PrimariaPrimariaPrimariaPrimaria',
            desc = 'Grado Primaria'
        )
        with self.assertRaises(ValidationError):
            cat_grado.full_clean()

    def test_desc_excede_limite_caracteres(self):
        cat_grado = CategoriaGrados.objects.create(
            nombre = 'PrimariaPrimariaPrimariaPrimaria',
            desc = 'Grado PGrado PrimariarimariaGrado PrimariaGrado PrimariaGrado PrimariaGrado PrimariaGrado PrimariaGrado PrimariaGrado PrimariaGrado PrimariaGrado Primaria'
        )
        with self.assertRaises(ValidationError):
            cat_grado.full_clean()
    
class EstadoModelTest(TestCase):
    def test_agregar_estado(self):
        estado = Estado.objects.create(
            nombre = "Zacatecas"
        )
        estado_uno = Estado.objects.first()

        self.assertEqual(estado, estado_uno)
        self.assertEqual(estado_uno.nombre, 'Zacatecas')
        self.assertEqual(str(estado_uno), 'Zacatecas')

    def test_nombre_excede_limite_caracteres(self):
        estado = Estado.objects.create(
            nombre = 'GuadalupeGuadalupeGuadalupeGuadalupeGuadalupeGuadalupeGuadalupeGuadalupeGuadalupeGuadalupeGuadalupeGuadalupe'
        )
        with self.assertRaises(ValidationError):
            estado.full_clean()

class MunicipioModelTest(TestCase):
    def setUp(self):
        self.estado = Estado.objects.create(
            nombre = "Zacatecas"
        )
    def test_agregar_municipio(self):
        
        municipio = Municipio.objects.create(
            estado = self.estado,
            nombre = 'Guadalupe'
        )
        municipio_uno = Municipio.objects.first()

        self.assertEqual(municipio, municipio_uno)
        self.assertEqual(municipio_uno.nombre, 'Guadalupe')
        self.assertEqual(str(municipio_uno), 'Guadalupe')

    def test_nombre_null(self):
        with self.assertRaises(IntegrityError):
            municipio = Municipio.objects.create(
                estado = self.estado,
                nombre = None
            )
            municipio.full_clean()

    def test_estado_null(self):
        with self.assertRaises(IntegrityError):
            municipio = Municipio.objects.create(
                estado = None,
                nombre = 'Guadalupe'
            )
            municipio.full_clean()

    def test_nombre_excede_limite_caracteres(self):
        municipio = Municipio.objects.create(
            estado = self.estado,
            nombre = 'GuadalupeGuadalupeGuadalupeGuadalupeGuadalupeGuadalupeGuadalupeGuadalupe'
        )
        with self.assertRaises(ValidationError):
            municipio.full_clean()

class EscuelaModelTest(TestCase):
    def test_agrega_escuela(self):
        escuela = Escuela.objects.create(nombre='Universidad Autónoma de Zacatecas', clave=125)
        una_escuela = Escuela.objects.first()

        self.assertEqual(escuela, una_escuela)
        self.assertEqual(una_escuela.nombre, 'Universidad Autónoma de Zacatecas')
        self.assertEqual(str(una_escuela), 'Universidad Autónoma de Zacatecas')

    def test_nombre_excede_longitud(self):
        escuela = Escuela.objects.create(
            nombre='Universidad Autónoma de Zacatecas Universidad Autónoma de Zacatecas Universidad Autónoma de Zacatecas Universidad Autónoma de Zacatecas Universidad Autónoma')
        with self.assertRaises(ValidationError):
            escuela.full_clean()

    def test_nombre_null(self):
        with self.assertRaises(IntegrityError):
            escuela = Escuela.objects.create(
                nombre = None
            )
            escuela.full_clean()

    def test_clave_exede_longitud(self):
        clave = Escuela.objects.create(clave=12345678910125551)
        with self.assertRaises(ValidationError):
            clave.full_clean()

    def test_incersion_de_escuela(self):
        escuela = Escuela.objects.create(nombre='Universidad Autónoma de Zacatecas')
        self.assertEquals(Escuela.objects.all()[0], escuela)

    def test_incersion_del_nombre_escuela(self):
        escuela = Escuela.objects.create(nombre='Universidad Autónoma de Zacatecas')
        escuela = Escuela.objects.first()
        self.assertEquals(escuela.nombre, 'Universidad Autónoma de Zacatecas')

class ProgramaModelTest(TestCase):
    def setUp(self):
        self.unidad_academica = UnidadAcademica.objects.create(nombre="Ingeniería Eléctrica")

    def test_agregar_programa(self):
        programa = Programa.objects.create(unidad_academica=self.unidad_academica,
                                           programa='Ingeniería de Software')
        programa_uno = Programa.objects.first()
        self.assertEqual(programa, programa_uno)
        self.assertEqual(programa_uno.programa, 'Ingeniería de Software')
        self.assertEqual(str(programa_uno), 'Ingeniería de Software')

    def test_nombre_null(self):
        with self.assertRaises(IntegrityError):
            programa = Programa.objects.create(
                unidad_academica = self.unidad_academica,
                programa = None
            )
            programa.full_clean()

    def test_unidad_academica_null(self):
        with self.assertRaises(IntegrityError):
            programa = UnidadAcademica.objects.create(
                nombre = None,
                programa = 'Ingeniería de Software'
            )
            programa.full_clean()

    def test_nombre_programa_exede_longitud(self):
        programa = Programa.objects.create(unidad_academica=self.unidad_academica,
                                           programa='Ingeniería de Software Ingeniería de Software Ingeniería de Software Ingeniería de Software Ingeniería de So')
        with self.assertRaises(ValidationError):
            programa.full_clean()

    def test_incersion_de_programa(self):
        programa = Programa.objects.create(unidad_academica=self.unidad_academica,
                                           programa='Ingeniería de Software')
        self.assertEquals(Programa.objects.all()[0], programa)

    def test_incersion_del_nombre_programa(self):
        programa = Programa.objects.create(unidad_academica=self.unidad_academica,
                                           programa='Ingeniería de Software')
        programa = Programa.objects.first()
        self.assertEquals(programa.programa, 'Ingeniería de Software')

class MateriaModelTest(TestCase):
    def setUp(self):
        self.unidad_academica = UnidadAcademica.objects.create(clave_antigua=1515, clave_nueva=515, nombre="Ciencias de la Salud")
        self.programa = Programa.objects.create(programa="Medicina Humana", unidad_academica=self.unidad_academica)

    def test_agregar_materia(self):
        materia = Materia.objects.create(programa=self.programa, nombre='Anatomía')
        una_materia = Materia.objects.first()
        self.assertEqual(materia, una_materia)
        self.assertEqual(una_materia.nombre, 'Anatomía')
        self.assertEqual(str(una_materia), 'Anatomía')

    def test_nombre_null(self):
        with self.assertRaises(IntegrityError):
            materia = Materia.objects.create(
                programa = self.programa,
                nombre = None
            )
            materia.full_clean()

    def test_nombre_materia_exede_longitud(self):
        materia = Materia.objects.create(programa=self.programa,
                                           nombre='Anatomía Ingeniería de Software Ingeniería de Software Ingeniería de Software Ingeniería de So')
        with self.assertRaises(ValidationError):
            materia.full_clean()

    def test_incersion_de_materia(self):
        materia = Materia.objects.create(programa=self.programa, nombre='Anatomía')
        self.assertEquals(Materia.objects.all()[0], materia)

    def test_incersion_del_nombre_materia(self):
        materia = Materia.objects.create(programa=self.programa,
                                           nombre='Anatomía')
        materia = Materia.objects.first()
        self.assertEquals(materia.nombre, 'Anatomía')

    def test_clave_exede_longitud(self):
        clave = Materia.objects.create(programa=self.programa, clave=123456789101255515154151212312121)
        with self.assertRaises(ValidationError):
            clave.full_clean()

    def test_incersion_de_clave(self):
        clave = Materia.objects.create(programa=self.programa, clave=5151521)
        self.assertEquals(Materia.objects.all()[0], clave)

class DatosPersonalesModelTest(TestCase):
    def setUp(self):
        estado = Estado.objects.create(
            nombre = 'Zacatecas'
        )
        municipio = Municipio.objects.create(
            estado = estado,
            nombre = 'Fresnillo'
        )

    def test_datos_personales_municipio_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento='1997-02-11',
                rfc='GUVM970211MZ7',
                curp='GUVM97021MZSTLT09',
                nss='12121',
                sexo='MUJER',
                estado_civil='SOLTERO',
                domicilio='Jose Ma. Coss #26',
                municipio=None,
                status=True
            )
            datos_personales.full_clean()

    def test_datos_personales_nombres_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres=None,
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento='1997-02-11',
                rfc='GUVM970211MZ7',
                curp='GUVM97021MZSTLT09',
                nss='12121',
                sexo='MUJER',
                estado_civil='SOLTERO',
                domicilio='Jose Ma. Coss #26',
                status=True
            )
            datos_personales.full_clean()

    def test_datos_personales_apellidos_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno=None,
                ap_materno=None,
                fecha_nacimiento='1997-02-11',
                rfc='GUVM970211MZ7',
                curp='GUVM97021MZSTLT09',
                nss='12121',
                sexo='MUJER',
                estado_civil='SOLTERO',
                domicilio='Jose Ma. Coss #26',
                status=True
            )
            datos_personales.full_clean()

    def test_datos_personales_fecha_nacimiento_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento=None,
                rfc='GUVM970211MZ7',
                curp='GUVM97021MZSTLT09',
                nss='12121',
                sexo='MUJER',
                estado_civil='SOLTERO',
                domicilio='Jose Ma. Coss #26',
                status=True
            )
            datos_personales.full_clean()

    def test_datos_personales_rfc_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento='1997-02-11',
                rfc=None,
                curp='GUVM97021MZSTLT09',
                nss='12121',
                sexo='MUJER',
                estado_civil='SOLTERO',
                domicilio='Jose Ma. Coss #26',
                status=True
            )
            datos_personales.full_clean()

    def test_datos_personales_curp_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento='1997-02-11',
                rfc='GUVM970211MZ7',
                curp=None,
                nss='12121',
                sexo='MUJER',
                estado_civil='SOLTERO',
                domicilio='Jose Ma. Coss #26',
                status=True
            )
            datos_personales.full_clean()

    def test_datos_personales_nss_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento='1997-02-11',
                rfc='GUVM970211MZ7',
                curp='GUVM97021MZSTLT09',
                nss=None,
                sexo='MUJER',
                estado_civil='SOLTERO',
                domicilio='Jose Ma. Coss #26',
                status=True
            )
            datos_personales.full_clean()

    def test_datos_personales_sexo_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento='1997-02-11',
                rfc='GUVM970211MZ7',
                curp='GUVM97021MZSTLT09',
                nss='12121',
                sexo=None,
                estado_civil='SOLTERO',
                domicilio='Jose Ma. Coss #26',
                status=True
            )
            datos_personales.full_clean()

    def test_datos_personales_estado_civil_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento='1997-02-11',
                rfc='GUVM970211MZ7',
                curp='GUVM97021MZSTLT09',
                nss='12121',
                sexo='MUJER',
                estado_civil=None,
                domicilio='Jose Ma. Coss #26',
                status=True
            )
            datos_personales.full_clean()

    def test_datos_personales_domicilio_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento='1997-02-11',
                rfc='GUVM970211MZ7',
                curp='GUVM97021MZSTLT09',
                nss='12121',
                sexo='MUJER',
                estado_civil='SOLTERO',
                domicilio=None,
                status=True
            )
            datos_personales.full_clean()

    def test_datos_personales_status_null(self):
        with self.assertRaises(IntegrityError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento='1997-02-11',
                rfc='GUVM970211MZ7',
                curp='GUVM97021MZSTLT09',
                nss='12121',
                sexo='MUJER',
                estado_civil='SOLTERO',
                domicilio='Jose Ma. Coss #26',
                status=None
            )
            datos_personales.full_clean()

    def test_fecha_nacimiento_formato_erroneo(self):
        with self.assertRaises(ValidationError):
            datos_personales = DatosPersonales.objects.create(
                nombres='Viridiana',
                ap_paterno='Gutiérrez',
                ap_materno='Villalobos',
                fecha_nacimiento='201212-12',
                rfc='GUVM970211MZ7',
                curp='GUVM97021MZSTLT09',
                nss='12121',
                sexo='MUJER',
                estado_civil='SOLTERO',
                domicilio='Jose Ma. Coss #26',
                status=None
            )
            datos_personales.full_clean()

class InterrupcionModelTest(TestCase):
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
        categoria_incidencia = CategoriaIncidencias.objects.create(
            permiso = 'PERMISO CON GOSE DE SALARIO',
            clausula = 65
        )
        self.incidencia = DocenteIncidencia.objects.create(
            docente = self.datos_personales,
            categoria_incidencia = categoria_incidencia,
            fecha_inicio = '2012-12-12',
            fecha_fin = '2012-12-12',
            imagen_incidencia = 'D:\Pictures\Diseños finales\Mtn.jpg'
        )
        self.unidad_academica = UnidadAcademica.objects.create(nombre="Ingeniería Eléctrica")

    def test_agregar_interrupcion(self):
        interrupcion = Interrupcion.objects.create(
            docente = self.datos_personales,
            incidencias = self.incidencia,
            fecha_inicio = '2012-12-12',
            fecha_fin = '2012-12-12',
            imagen_interrupcion = 'D:\Pictures\Diseños finales\Mtn.jpg'
        )
        interrupcion_uno = Interrupcion.objects.first()
        self.assertEqual(interrupcion, interrupcion_uno)
        self.assertEqual(str(interrupcion_uno), 'José Andrés Muro Vargas 2012-12-12 2012-12-12')

    def test_interrupcion_datos_personales_null(self):
        with self.assertRaises(IntegrityError):
            interrupcion = Interrupcion.objects.create(
                docente = None,
                incidencias = self.incidencia,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12',
                imagen_interrupcion = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            interrupcion.full_clean()

    def test_interrupcion_incidencias_null(self):
        with self.assertRaises(IntegrityError):
            interrupcion = Interrupcion.objects.create(
                docente = self.datos_personales,
                incidencias = None,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12',
                imagen_interrupcion = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            interrupcion.full_clean()

    def test_interrupcion_fecha_inicio_null(self):
        with self.assertRaises(IntegrityError):
            interrupcion = Interrupcion.objects.create(
                docente = self.datos_personales,
                incidencias = self.incidencia,
                fecha_inicio = None,
                fecha_fin = '2012-12-12',
                imagen_interrupcion = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            interrupcion.full_clean()

    def test_interrupcion_fecha_fin_null(self):
        with self.assertRaises(IntegrityError):
            interrupcion = Interrupcion.objects.create(
                docente = self.datos_personales,
                incidencias = self.incidencia,
                fecha_inicio = '2012-12-12',
                fecha_fin = None,
                imagen_interrupcion = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            interrupcion.full_clean()

    def test_interrupcion_imagen_null(self):
        with self.assertRaises(ValidationError):
            interrupcion = Interrupcion.objects.create(
                docente = self.datos_personales,
                incidencias = self.incidencia,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12',
                imagen_interrupcion = None
            )
            interrupcion.full_clean()

    def test_interrupcion_fecha_inicio_formato_incorrecto(self):
        with self.assertRaises(ValidationError):
            interrupcion = Interrupcion.objects.create(
                docente = self.datos_personales,
                incidencias = self.incidencia,
                fecha_inicio = '2012-1212',
                fecha_fin = '2012-12-12',
                imagen_interrupcion = None
            )
            interrupcion.full_clean()

    def test_interrupcion_fecha_fin_formato_incorrecto(self):
        with self.assertRaises(ValidationError):
            interrupcion = Interrupcion.objects.create(
                docente = self.datos_personales,
                incidencias = self.incidencia,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-1212',
                imagen_interrupcion = None
            )
            interrupcion.full_clean()

class DocenteIncidenciasModelTest(TestCase):
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
        self.categoria_incidencia = CategoriaIncidencias.objects.create(
            permiso = 'PERMISO CON GOSE DE SALARIO',
            clausula = 65
        )

        self.unidad_academica = UnidadAcademica.objects.create(nombre="Ingeniería Eléctrica")

    def test_agregar_incidencia(self):
        incidencia = DocenteIncidencia.objects.create(
            docente = self.datos_personales,
            categoria_incidencia = self.categoria_incidencia,
            fecha_inicio = '2012-12-12',
            fecha_fin = '2012-12-12',
            imagen_incidencia = 'D:\Pictures\Diseños finales\Mtn.jpg'
        )
        incidencia_uno = DocenteIncidencia.objects.first()
        self.assertEqual(incidencia, incidencia_uno)
        self.assertEqual(str(incidencia_uno), 'PERMISO CON GOSE DE SALARIO José Andrés Muro Vargas 2012-12-12-2012-12-12')

    def test_incidencia_docente_null(self):
        with self.assertRaises(IntegrityError):
            incidencia = DocenteIncidencia.objects.create(
                docente = None,
                categoria_incidencia = self.categoria_incidencia,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12',
                imagen_incidencia = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            incidencia.full_clean()

    def test_incidencia_categoria_incidencia_null(self):
        with self.assertRaises(IntegrityError):
            incidencia = DocenteIncidencia.objects.create(
                docente = self.datos_personales,
                categoria_incidencia = None,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12',
                imagen_incidencia = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            incidencia.full_clean()

    def test_incidencia_fecha_inicio_null(self):
        with self.assertRaises(IntegrityError):
            incidencia = DocenteIncidencia.objects.create(
                docente = self.datos_personales,
                categoria_incidencia = self.categoria_incidencia,
                fecha_inicio = None,
                fecha_fin = '2012-12-12',
                imagen_incidencia = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            incidencia.full_clean()

    def test_incidencia_fecha_fin_null(self):
        with self.assertRaises(IntegrityError):
            incidencia = DocenteIncidencia.objects.create(
                docente = self.datos_personales,
                categoria_incidencia = self.categoria_incidencia,
                fecha_inicio = '2012-12-12',
                fecha_fin = None,
                imagen_incidencia = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            incidencia.full_clean()

    def test_incidencia_imagen_null(self):
        with self.assertRaises(ValidationError):
            incidencia = DocenteIncidencia.objects.create(
                docente = self.datos_personales,
                categoria_incidencia = self.categoria_incidencia,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12',
                imagen_incidencia = None
            )
            incidencia.full_clean()

    def test_incidencia_fecha_inicio_formato_incorrecto(self):
        with self.assertRaises(ValidationError):
            incidencia = DocenteIncidencia.objects.create(
                docente = self.datos_personales,
                categoria_incidencia = self.categoria_incidencia,
                fecha_inicio = '2012-1212',
                fecha_fin = '2012-12-12',
                imagen_incidencia = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            incidencia.full_clean()

    def test_incidencia_fecha_fin_formato_incorrecto(self):
        with self.assertRaises(ValidationError):
            incidencia = DocenteIncidencia.objects.create(
                docente = self.datos_personales,
                categoria_incidencia = self.categoria_incidencia,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-1212',
                imagen_incidencia = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            incidencia.full_clean()

class CuerpoAcademicoModelTest(TestCase):
    def setUp(self):
        self.unidad_academica = UnidadAcademica.objects.create(nombre="Ingeniería Eléctrica")

    def test_agregar_cuerpo_academico(self):
        cuerpo = CuerpoAcademico.objects.create(
            no_registro = 123,
            nombre = 'UAZ',
            unidad_academica = self.unidad_academica,
            fecha_inicio = '2012-12-12',
            fecha_fin = '2012-12-12'
        )
        cuerpo_uno = CuerpoAcademico.objects.first()
        self.assertEqual(cuerpo, cuerpo_uno)
        self.assertEqual(cuerpo_uno.no_registro, '123')
        self.assertEqual(str(cuerpo_uno), 'UAZ')

    def test_cuerpo_no_registro_null(self):
        with self.assertRaises(IntegrityError):
            cuerpo = CuerpoAcademico.objects.create(
                no_registro = None,
                nombre = 'UAZ',
                unidad_academica = self.unidad_academica,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12'
            )
            cuerpo.full_clean()

    def test_cuerpo_nombre_null(self):
        with self.assertRaises(IntegrityError):
            cuerpo = CuerpoAcademico.objects.create(
                no_registro = 123,
                nombre = None,
                unidad_academica = self.unidad_academica,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12'
            )
            cuerpo.full_clean()

    def test_cuerpo_unidad_null(self):
        with self.assertRaises(IntegrityError):
            cuerpo = CuerpoAcademico.objects.create(
                no_registro = 123,
                nombre = 'UAZ',
                unidad_academica = None,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12'
            )
            cuerpo.full_clean()

    def test_cuerpo_fecha_inicio_null(self):
        with self.assertRaises(IntegrityError):
            cuerpo = CuerpoAcademico.objects.create(
                no_registro = 123,
                nombre = 'UAZ',
                unidad_academica = self.unidad_academica,
                fecha_inicio = None,
                fecha_fin = '2012-12-12'
            )
            cuerpo.full_clean()

    def test_cuerpo_fecha_fin_null(self):
        with self.assertRaises(IntegrityError):
            cuerpo = CuerpoAcademico.objects.create(
                no_registro = 123,
                nombre = 'UAZ',
                unidad_academica = self.unidad_academica,
                fecha_inicio = '2012-12-12',
                fecha_fin = None
            )
            cuerpo.full_clean()

    def test_cuerpo_fecha_inicio_formato_incorrecto(self):
        with self.assertRaises(ValidationError):
            cuerpo = CuerpoAcademico.objects.create(
                no_registro = 123,
                nombre = 'UAZ',
                unidad_academica = self.unidad_academica,
                fecha_inicio = '2012-1212',
                fecha_fin = '2012-12-12'
            )
            cuerpo.full_clean()

    def test_cuerpo_fecha_fin_formato_incorrecto(self):
        with self.assertRaises(ValidationError):
            cuerpo = CuerpoAcademico.objects.create(
                no_registro = 123,
                nombre = 'UAZ',
                unidad_academica = self.unidad_academica,
                fecha_inicio = '2012-12-12',
                fecha_fin = '201212-12'
            )
            cuerpo.full_clean()

    def test_no_registro_excede_limite_de_caracteres(self):
        cuerpo = CuerpoAcademico.objects.create(
                no_registro = 123123123123123123123,
                nombre = 'UAZ',
                unidad_academica = self.unidad_academica,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12'
            )
        with self.assertRaises(ValidationError):
            cuerpo.full_clean()

    def test_nombre_limite_de_caracteres(self):
        cuerpo = CuerpoAcademico.objects.create(
                no_registro = 121,
                nombre = 'UAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZUAZ',
                unidad_academica = self.unidad_academica,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12'
            )
        with self.assertRaises(ValidationError):
            cuerpo.full_clean()

class DatosLaboralesModelTest(TestCase):
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
        self.categoria_incidencia = CategoriaIncidencias.objects.create(
            permiso = 'PERMISO CON GOSE DE SALARIO',
            clausula = 65
        )
        self.unidad_academica = UnidadAcademica.objects.create(
            nombre="Ingeniería Eléctrica"
        )
        self.cuerpo = CuerpoAcademico.objects.create(
                no_registro = 123,
                nombre = 'UAZ',
                unidad_academica = self.unidad_academica,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12'
            )

    def test_agregar_datos_laborales(self):
        datos_laborales = DatosLaborales.objects.create(
            datos_personales = self.datos_personales,
            matricula_docente = '1234',
            matricula_nomina = '123345',
            fecha_ingreso = '2012-12-12',
            no_expediente = 123.12,
            exclusivo = False,
            cuerpo_academico = self.cuerpo
        )
        datos_laborales_uno = DatosLaborales.objects.first()
        self.assertEqual(datos_laborales, datos_laborales_uno)
        self.assertEqual(str(datos_laborales_uno), 'Datos laborales de José Andrés Muro Vargas')

    def test_datos_laborales_datos_personales_null(self):
        with self.assertRaises(IntegrityError):
            datos_laborales = DatosLaborales.objects.create(
                datos_personales = None,
                matricula_docente = '1234',
                matricula_nomina = '123345',
                fecha_ingreso = '2012-12-12',
                no_expediente = 123.12,
                exclusivo = False,
                cuerpo_academico = self.cuerpo
            )
            datos_laborales.full_clean()

    def test_datos_laborales_matricula_docente_null(self):
        with self.assertRaises(IntegrityError):
            datos_laborales = DatosLaborales.objects.create(
                datos_personales = self.datos_personales,
                matricula_docente = None,
                matricula_nomina = '123345',
                fecha_ingreso = '2012-12-12',
                no_expediente = 123.12,
                exclusivo = False,
                cuerpo_academico = self.cuerpo
            )
            datos_laborales.full_clean()

    def test_datos_laborales_matricula_nomina_null(self):
        with self.assertRaises(IntegrityError):
            datos_laborales = DatosLaborales.objects.create(
                datos_personales =self.datos_personales,
                matricula_docente = '1234',
                matricula_nomina = None,
                fecha_ingreso = '2012-12-12',
                no_expediente = 123.12,
                exclusivo = False,
                cuerpo_academico = self.cuerpo
            )
            datos_laborales.full_clean()

    def test_datos_laborales_fecha_ingreso_null(self):
        with self.assertRaises(IntegrityError):
            datos_laborales = DatosLaborales.objects.create(
                datos_personales = self.datos_personales,
                matricula_docente = '1234',
                matricula_nomina = '123345',
                fecha_ingreso = None,
                no_expediente = 123.12,
                exclusivo = False,
                cuerpo_academico = self.cuerpo
            )
            datos_laborales.full_clean()

    def test_datos_laborales_no_expediente_null(self):
        with self.assertRaises(ValidationError):
            datos_laborales = DatosLaborales.objects.create(
                datos_personales = self.datos_personales,
                matricula_docente = '1234',
                matricula_nomina = '123345',
                fecha_ingreso = '2012-12-12',
                no_expediente = None,
                exclusivo = False,
                cuerpo_academico = self.cuerpo
            )
            datos_laborales.full_clean()

    def test_datos_laborales_exclusivo_null(self):
        with self.assertRaises(IntegrityError):
            datos_laborales = DatosLaborales.objects.create(
                datos_personales = self.datos_personales,
                matricula_docente = '1234',
                matricula_nomina = '123345',
                fecha_ingreso = '2012-12-12',
                no_expediente = 123.12,
                exclusivo = None,
                cuerpo_academico = self.cuerpo
            )
            datos_laborales.full_clean()

    def test_datos_laborales_cuerpo_academico_null(self):
        with self.assertRaises(ValidationError):
            datos_laborales = DatosLaborales.objects.create(
                datos_personales = self.datos_personales,
                matricula_docente = '1234',
                matricula_nomina = '123345',
                fecha_ingreso = '2012-12-12',
                no_expediente = 123.12,
                exclusivo = False,
                cuerpo_academico = None
            )
            datos_laborales.full_clean()

    def test_matricula_docente_excede_limite_de_caracteres(self):
        datos_laborales = DatosLaborales.objects.create(
            datos_personales = self.datos_personales,
            matricula_docente = '12234',
            matricula_nomina = '123345',
            fecha_ingreso = '2012-12-12',
            no_expediente = 123.12,
            exclusivo = False,
            cuerpo_academico = self.cuerpo
        )
        with self.assertRaises(ValidationError):
            datos_laborales.full_clean()

    def test_matricula_nomina_excede_limite_de_caracteres(self):
        datos_laborales = DatosLaborales.objects.create(
            datos_personales = self.datos_personales,
            matricula_docente = '1234',
            matricula_nomina = '12331245',
            fecha_ingreso = '2012-12-12',
            no_expediente = 123.12,
            exclusivo = False,
            cuerpo_academico = self.cuerpo
        )
        with self.assertRaises(ValidationError):
            datos_laborales.full_clean()

    def test_no_expediente_excede_limite_de_caracteres(self):
        with self.assertRaises(InvalidOperation):
            datos_laborales = DatosLaborales.objects.create(
                datos_personales = self.datos_personales,
                matricula_docente = '1234',
                matricula_nomina = '123345',
                fecha_ingreso = '2012-12-12',
                no_expediente = 123211,
                exclusivo = False,
                cuerpo_academico = self.cuerpo
            )
            datos_laborales.full_clean()

    def test_fecha_ingreso_formato_erroneo(self):
        with self.assertRaises(ValidationError):
            datos_laborales = DatosLaborales.objects.create(
                datos_personales = self.datos_personales,
                matricula_docente = '1234',
                matricula_nomina = '123345',
                fecha_ingreso = '201212-12',
                no_expediente = 123.12,
                exclusivo = False,
                cuerpo_academico = self.cuerpo
            )
            datos_laborales.full_clean()

class GradoAcademicoModelTest(TestCase):
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
        self.categoria_incidencia = CategoriaIncidencias.objects.create(
            permiso = 'PERMISO CON GOSE DE SALARIO',
            clausula = 65
        )
        self.unidad_academica = UnidadAcademica.objects.create(
            nombre="Ingeniería Eléctrica"
        )
        self.cuerpo = CuerpoAcademico.objects.create(
                no_registro = 123,
                nombre = 'UAZ',
                unidad_academica = self.unidad_academica,
                fecha_inicio = '2012-12-12',
                fecha_fin = '2012-12-12'
        )
        self.escuela = Escuela.objects.create(
            nombre='Universidad Autónoma de Zacatecas', clave=125
        )

    def test_agregar_grado_academico(self):
        grado_academico = GradosAcademicos.objects.create(
            docente = self.datos_personales,
            escuela = self.escuela,
            fecha_obtencion = '2012-12-12',
            categoria_grados = 'BACHILLERATO',
            nombre_estudio = 'PREPA',
            imagen_grado = 'D:\Pictures\Diseños finales\Mtn.jpg'
        )
        grado_academico_uno = GradosAcademicos.objects.first()
        self.assertEqual(grado_academico, grado_academico_uno)
        self.assertEqual(str(grado_academico_uno), 'PREPA José Andrés Muro Vargas')

    def test_grado_academico_docente_null(self):
        with self.assertRaises(IntegrityError):
            grado_academico = GradosAcademicos.objects.create(
                docente = None,
                escuela = self.escuela,
                fecha_obtencion = '2012-12-12',
                categoria_grados = 'BACHILLERATO',
                nombre_estudio = 'PREPA',
                imagen_grado = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            grado_academico.full_clean()

    def test_grado_academico_escuela_null(self):
        with self.assertRaises(IntegrityError):
            grado_academico = GradosAcademicos.objects.create(
                docente = self.datos_personales,
                escuela = None,
                fecha_obtencion = '2012-12-12',
                categoria_grados = 'BACHILLERATO',
                nombre_estudio = 'PREPA',
                imagen_grado = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            grado_academico.full_clean()

    def test_grado_academico_fecha_obtencion_null(self):
        with self.assertRaises(IntegrityError):
            grado_academico = GradosAcademicos.objects.create(
                docente = self.datos_personales,
                escuela = self.escuela,
                fecha_obtencion = None,
                categoria_grados = 'BACHILLERATO',
                nombre_estudio = 'PREPA',
                imagen_grado = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            grado_academico.full_clean()

    def test_grado_academico_categoria_grados_null(self):
        with self.assertRaises(IntegrityError):
            grado_academico = GradosAcademicos.objects.create(
                docente = self.datos_personales,
                escuela = self.escuela,
                fecha_obtencion = '2012-12-12',
                categoria_grados = None,
                nombre_estudio = 'PREPA',
                imagen_grado = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            grado_academico.full_clean()

    def test_grado_academico_nombre_estudio_null(self):
        with self.assertRaises(IntegrityError):
            grado_academico = GradosAcademicos.objects.create(
                docente = self.datos_personales,
                escuela = self.escuela,
                fecha_obtencion = '2012-12-12',
                categoria_grados = 'BACHILLERATO',
                nombre_estudio = None,
                imagen_grado = 'D:\Pictures\Diseños finales\Mtn.jpg'
            )
            grado_academico.full_clean()

    # def test_grado_academico_imagen_grado_null(self):
    #     with self.assertRaises(ValidationError):
    #         grado_academico = GradosAcademicos.objects.create(
    #             docente = self.datos_personales,
    #             escuela = self.escuela,
    #             fecha_obtencion = '2012-12-12',
    #             categoria_grados = 'BACHILLERATO',
    #             nombre_estudio = 'PREPA',
    #             imagen_grado = None
    #         )
    #         grado_academico.full_clean()

    def test_nombre_estudio_excede_limite_de_caracteres(self):
        grado_academico = GradosAcademicos.objects.create(
            docente = self.datos_personales,
            escuela = self.escuela,
            fecha_obtencion = '2012-12-12',
            categoria_grados = 'BACHILLERATO',
            nombre_estudio = 'PREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAPREPAs',
            imagen_grado = 'D:\Pictures\Diseños finales\Mtn.jpg'
        )
        with self.assertRaises(ValidationError):
            grado_academico.full_clean()

    def test_fecha_obtencion_formato_erroneo(self):
        with self.assertRaises(ValidationError):
            grado_academico = GradosAcademicos.objects.create(
                docente = self.datos_personales,
                escuela = self.escuela,
                fecha_obtencion = '201212-12',
                categoria_grados = 'BACHILLERATO',
                nombre_estudio = 'PREPA',
                imagen_grado = None
            )
            grado_academico.full_clean()


class CategoriaIncidenciasModelTest(TestCase):

    def test_agregar_categoria_incidencias_datos_correctos(self):
        cat_incidencia = CategoriaIncidencias.objects.create(
            permiso='DESCANSO Y BONO POR MATERNIDAD',
            clausula=63
        )

        cat_incidencia_primera = CategoriaIncidencias.objects.first()

        self.assertEqual(cat_incidencia, cat_incidencia_primera)
        self.assertEqual(cat_incidencia.permiso, cat_incidencia_primera.permiso)
        self.assertEqual(cat_incidencia.clausula, cat_incidencia_primera.clausula)

    def test_permiso_excede_limite_caracteres(self):
        cat_incidencia = CategoriaIncidencias.objects.create(
            permiso='DESCANSO Y BONO POR MATERNIDAD DESCANSO Y BONO POR MATERNIDAD DESCANSO Y BONO POR MATERNIDAD DESCANSO Y BONO POR MATERNIDAD DESCANSO Y BONO POR MATERNIDAD',
            clausula='63'
        )
        with self.assertRaises(ValidationError):
            cat_incidencia.full_clean()

    def test_categoria_incidencia_permiso_null(self):
        with self.assertRaises(IntegrityError):
            cat_incidencia = CategoriaIncidencias.objects.create(
                permiso=None,
                clausula='63'
            )
            cat_incidencia.full_clean()

class UnidadAcademicaModelTest(TestCase):

    def test_agregar_unidad_academica_datos_correctos(self):
        unidad_academica = UnidadAcademica.objects.create(
            clave_nueva='132',
            clave_antigua='312',
            nombre='Ingeniería Eléctrica'
        )

        unidad_academica_primera = UnidadAcademica.objects.first()

        self.assertEqual(unidad_academica, unidad_academica_primera)
        self.assertEqual(unidad_academica.clave_nueva, unidad_academica_primera.clave_nueva)
        self.assertEqual(unidad_academica.clave_antigua, unidad_academica_primera.clave_antigua)
        self.assertEqual(unidad_academica.nombre, unidad_academica_primera.nombre)

    def test_unidad_academica_nombre_excede_limite_caracteres(self):
        unidad_academica = UnidadAcademica.objects.create(
            clave_nueva='132',
            clave_antigua='312',
            nombre='Ingeniería Eléctrica Ingeniería Eléctrica Ingeniería Eléctrica Ingeniería Eléctrica Ingeniería Eléctrica'
        )
        with self.assertRaises(ValidationError):
            unidad_academica.full_clean()

    def test_unidad_academica_nombre_null(self):
        with self.assertRaises(IntegrityError):
            unidad_academica = UnidadAcademica.objects.create(
                clave_nueva='132',
                clave_antigua='312',
                nombre=None
            )
            unidad_academica.full_clean()

    def test_unidad_academica_clave_nueva_null(self):
        with self.assertRaises(IntegrityError):
            unidad_academica = UnidadAcademica.objects.create(
                clave_nueva = None,
                clave_antigua='312',
                nombre='Unidad Académica de Derecho'
            )
            unidad_academica.full_clean()

class ProdepModelTest(TestCase):
    def setUp(self):
        estado = Estado.objects.create(
            nombre="Zacatecas"
        )

        municipio = Municipio.objects.create(
            estado=estado,
            nombre='Valparaíso'
        )

        self.docente = DatosPersonales.objects.create(
            nombres='Pedro Angel',
            ap_paterno='Sanchez',
            ap_materno='Hinostroza',
            fecha_nacimiento='1998-10-07',
            rfc='SAHP981007KF7',
            curp='SAHP981007HZSNND03',
            nss='123412',
            sexo= SEXO[0],
            estado_civil=ESTADO_CIVIL[1],
            domicilio='Netzahualcoyotl 107 Col. Los Guerreros',
            municipio=municipio,
            status=True
        )

    def test_agregar_prodep_datos_correctos(self):
        prodep = Prodep.objects.create(
            docente = self.docente,
            clave = '321412',
            descripcion = 'Desarrollo de una aplicación web para ayudar a la gente',
            fecha_inicio_prodep=datetime.date(2018, 9, 9),
            fecha_fin_prodep=datetime.date(2019, 3, 12),
            imagen_prodep = 'images/prodep1.jpg'
        )

        prodep_primero = Prodep.objects.first()

        self.assertEqual(prodep, prodep_primero)
        self.assertEqual(prodep.docente, prodep_primero.docente)
        self.assertEqual(prodep.clave, prodep_primero.clave)
        self.assertEqual(prodep.descripcion, prodep_primero.descripcion)
        self.assertEqual(prodep.fecha_inicio_prodep, prodep_primero.fecha_inicio_prodep)
        self.assertEqual(prodep.fecha_fin_prodep, prodep_primero.fecha_fin_prodep)
        self.assertEqual(prodep.imagen_prodep, prodep_primero.imagen_prodep)

    def test_clave_prodep_excede_limite_caracteres(self):
        prodep = Prodep.objects.create(
            docente=self.docente,
            clave='3243424515435353265463563563456437656542235423632464354325432652435523454325432542351412',
            descripcion='Desarrollo de una aplicación web para ayudar a la gente',
            fecha_inicio_prodep=datetime.date(2018, 9, 9),
            fecha_fin_prodep=datetime.date(2019, 3, 12),
            imagen_prodep='images/prodep1.jpg'
        )
        with self.assertRaises(ValidationError):
            prodep.full_clean()

    # def test_clave_prodep_null(self):
    #     with self.assertRaises(IntegrityError):
    #         prodep = Prodep.objects.create(
    #             docente=self.docente,
    #             clave=None,
    #             descripcion='Desarrollo de una aplicación web para ayudar a la gente',
    #             fecha_inicio_prodep=datetime.date(2018, 9, 9),
    #             fecha_fin_prodep=datetime.date(2019, 3, 12),
    #             imagen_prodep='images/prodep1.jpg'
    #         )
    #         prodep.full_clean()

    # def test_prodep_fecha_inicio_null(self):
    #     with self.assertRaises(IntegrityError):
    #         prodep = Prodep.objects.create(
    #             docente=self.docente,
    #             clave='321412',
    #             descripcion='Desarrollo de una aplicación web para ayudar a la gente',
    #             fecha_inicio_prodep=None,
    #             fecha_fin_prodep=datetime.date(2019, 3, 12),
    #             imagen_prodep='images/prodep1.jpg'
    #         )
    #         prodep.full_clean()

    # def test_prodep_fecha_fin_null(self):
    #     with self.assertRaises(IntegrityError):
    #         prodep = Prodep.objects.create(
    #             docente=self.docente,
    #             clave='321412',
    #             descripcion='Desarrollo de una aplicación web para ayudar a la gente',
    #             fecha_inicio_prodep=datetime.date(2018, 9, 9),
    #             fecha_fin_prodep=None,
    #             imagen_prodep='images/prodep1.jpg'
    #         )
    #         prodep.full_clean()

    def test_prodep_imagen_null(self):
        prodep = Prodep.objects.create(
            docente=self.docente,
            clave='3243424515435353265463563563456437656542235423632464354325432652435523454325432542351412',
            descripcion='Desarrollo de una aplicación web para ayudar a la gente',
            fecha_inicio_prodep=datetime.date(2018, 9, 9),
            fecha_fin_prodep=datetime.date(2019, 3, 12),
            imagen_prodep=None
        )
        with self.assertRaises(ValidationError):
            prodep.full_clean()

class SniModelTest(TestCase):
    def setUp(self):
        estado = Estado.objects.create(
            nombre="Zacatecas"
        )

        municipio = Municipio.objects.create(
            estado=estado,
            nombre='Valparaíso'
        )

        self.docente = DatosPersonales.objects.create(
            nombres='Pedro Angel',
            ap_paterno='Sanchez',
            ap_materno='Hinostroza',
            fecha_nacimiento='1998-10-07',
            rfc='SAHP981007KF7',
            curp='SAHP981007HZSNND03',
            nss='123412',
            sexo= SEXO[0],
            estado_civil=ESTADO_CIVIL[1],
            domicilio='Netzahualcoyotl 107 Col. Los Guerreros',
            municipio=municipio,
            status=True
        )

    def test_agregar_sni_datos_correctos(self):
        sni = Sni.objects.create(
            docente=self.docente,
            clave='321412',
            descripcion='Sesiones extra a alumnos con bajo rendimiento',
            fecha_inicio_sni=datetime.date(2018, 10, 10),
            fecha_fin_sni=datetime.date(2019, 10, 10),
            nivel=NIVELES_SNI[1],
            imagen_sni='images/sni1.jpg'
        )

        sni_primero = Sni.objects.first()

        self.assertEqual(sni, sni_primero)
        self.assertEqual(sni.docente, sni_primero.docente)
        self.assertEqual(sni.clave, sni_primero.clave)
        self.assertEqual(sni.descripcion, sni_primero.descripcion)
        self.assertEqual(sni.fecha_inicio_sni, sni_primero.fecha_inicio_sni)
        self.assertEqual(sni.fecha_fin_sni, sni_primero.fecha_fin_sni)
        self.assertEqual(str(sni.nivel), str(sni_primero.nivel))
        self.assertEqual(sni.imagen_sni, sni_primero.imagen_sni)

    def test_clave_sni_excede_limite_caracteres(self):
        sni = Sni.objects.create(
            docente=self.docente,
            clave='3243424515435353265463563563456437656542235423632464354325432652435523454325432542351412',
            descripcion='Sesiones extra a alumnos con bajo rendimiento',
            fecha_inicio_sni=datetime.date(2018, 9, 9),
            fecha_fin_sni=datetime.date(2019, 3, 12),
            nivel=NIVELES_SNI[1],
            imagen_sni='images/sni1.jpg'
        )
        with self.assertRaises(ValidationError):
            sni.full_clean()

    def test_nivel_no_correspone_a_las_opciones(self):
        sni = Sni.objects.create(
            docente=self.docente,
            clave='321412',
            descripcion='Sesiones extra a alumnos con bajo rendimiento',
            fecha_inicio_sni=datetime.date(2018, 10, 10),
            fecha_fin_sni=datetime.date(2019, 10, 10),
            nivel='Nivel inventado',
            imagen_sni='images/sni1.jpg'
        )
        with self.assertRaises(ValidationError):
            sni.full_clean()

    # def test_clave_sni_null(self):
    #     with self.assertRaises(IntegrityError):
    #         sni = Sni.objects.create(
    #             docente=self.docente,
    #             clave=None,
    #             descripcion='Sesiones extra a alumnos con bajo rendimiento',
    #             fecha_inicio_sni=datetime.date(2018, 9, 9),
    #             fecha_fin_sni=datetime.date(2019, 3, 12),
    #             nivel=NIVELES_SNI[1],
    #             imagen_sni='images/sni1.jpg'
    #         )
    #         sni.full_clean()

    def test_sni_imagen_null(self):
        sni = Sni.objects.create(
            docente=self.docente,
            clave='3243424515435353265463563563456437656542235423632464354325432652435523454325432542351412',
            descripcion='Sesiones extra a alumnos con bajo rendimiento',
            fecha_inicio_sni=datetime.date(2018, 9, 9),
            fecha_fin_sni=datetime.date(2019, 3, 12),
            imagen_sni=None
        )
        with self.assertRaises(ValidationError):
            sni.full_clean()

    # def test_sni_fecha_inicio_null(self):
    #     with self.assertRaises(IntegrityError):
    #         sni = Sni.objects.create(
    #             docente=self.docente,
    #             clave='321412',
    #             descripcion='Sesiones extra a alumnos con bajo rendimiento',
    #             fecha_inicio_sni=None,
    #             fecha_fin_sni=datetime.date(2019, 3, 12),
    #             imagen_sni='images/sni1.jpg'
    #         )
    #         sni.full_clean()

    # def test_sni_fecha_fin_null(self):
    #     with self.assertRaises(IntegrityError):
    #         sni = Sni.objects.create(
    #             docente=self.docente,
    #             clave='321412',
    #             descripcion='Sesiones extra a alumnos con bajo rendimiento',
    #             fecha_inicio_sni=datetime.date(2018, 9, 9),
    #             fecha_fin_sni=None,
    #             imagen_sni='images/sni1.jpg'
    #         )
    #         sni.full_clean()