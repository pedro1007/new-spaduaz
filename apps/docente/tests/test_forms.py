from django.test import TestCase
from apps.docente.forms import *
from apps.docente.models import *

class DatosPersonalesFormTest(TestCase):
    def setUp(self, nombres='', ap_paterno='', ap_materno='', fecha_nacimiento='', rfc='', curp='', nss='', sexo='', estado_civil='', domicilio='', municipio='', status=''):
        self.data = {
            'nombres': nombres,
            'ap_paterno': ap_paterno,
            'ap_materno': ap_materno,
            'fecha_nacimiento': fecha_nacimiento,
            'rfc': rfc,
            'curp': curp,
            'nss': nss,
            'sexo': sexo,
            'estado_civil': estado_civil,
            'domicilio': domicilio,
            'municipio': municipio,
            'status': status
        }

    def test_docente_nombre_vacio(self):
        estado = Estado.objects.create(
            nombre='Zacatecas'
        )
        municipio = Municipio.objects.create(
            estado=estado,
            nombre='Guadalupe'
        )
        datos_personales = DatosPersonales.objects.create(
            ap_paterno='Gutiérrez',
            ap_materno='Villalobos',
            fecha_nacimiento='1997-02-11',
            rfc='GUVM970211HU7',
            curp='GUVM970211MSTLT09',
            nss='4834',
            sexo='MUJER',
            estado_civil='SOLTERO',
            domicilio='Jose Ma. Coss #26',
            municipio=municipio,
            status=True
        )

        form = DatosPersonalesForm(
            data={
                'nombres': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_docente_apellidos_vacios(self):
        estado = Estado.objects.create(
            nombre='Zacatecas'
        )
        municipio = Municipio.objects.create(
            estado=estado,
            nombre='Guadalupe'
        )
        datos_personales = DatosPersonales.objects.create(
            nombres='Viridiana',
            fecha_nacimiento='1997-02-11',
            rfc='GUVM970211HU7',
            curp='GUVM970211MSTLT09',
            nss='4834',
            sexo='MUJER',
            estado_civil='SOLTERO',
            domicilio='Jose Ma. Coss #26',
            municipio=municipio,
            status=True
        )

        form = DatosPersonalesForm(
            data={
                'ap_paterno': '',
                'ap_materno': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_docente_rfc_curp_nss_vacios(self):
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
            sexo='MUJER',
            estado_civil='SOLTERO',
            domicilio='Jose Ma. Coss #26',
            municipio=municipio,
            status=True
        )

        form = DatosPersonalesForm(
            data={
                'rfc': '',
                'curp': '',
                'nss': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_docente_domicilio_vacio(self):
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
            sexo='MUJER',
            estado_civil='SOLTERO',
            municipio=municipio,
            status=True
        )

        form = DatosPersonalesForm(
            data={
                'domicilio': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_docente_sexo_es_civil_vacio(self):
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

        form = DatosPersonalesForm(
            data={
                'sexo': '',
                'estado_civil': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_docente_status_vacio(self):
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
            sexo='MUJER',
            estado_civil='SOLTERO',
            domicilio='Jose Ma. Coss #26',
            municipio=municipio,
        )

        form = DatosPersonalesForm(
            data={
                'status': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_max_length_apellido_paterno(self):
        self.data['ap_paterno'] = 'Gutiérrez sjdhjsahdkjsajdashdjasdjkhajkdhkjashdjkhasjdhsjvjakdvnsvmn'
        form = DatosPersonalesForm(
            self.data
        )
        self.assertEquals(form.errors['ap_paterno'], [LONGITUD_MAXIMA])

    def test_max_length_apellido_materno(self):
        self.data['ap_materno'] = 'Villalobos sjdhjsahdkjsajdashdjasdjkhajkdhkjashdjkhasjdhsjvjakdvnsvmn'
        form = DatosPersonalesForm(
            self.data
        )
        self.assertEquals(form.errors['ap_materno'], [LONGITUD_MAXIMA])

    def test_max_length_rfc(self):
        self.data['rfc'] = 'GUVM970211HU7 fdsfdfs'
        form = DatosPersonalesForm(
            self.data
        )
        self.assertEquals(form.errors['rfc'], [LONGITUD_MAXIMA])

    def test_max_length_curp(self):
        self.data['curp'] = 'GUVM970211MSTLT09 fdsfdfs'
        form = DatosPersonalesForm(
            self.data
        )
        self.assertEquals(form.errors['curp'], [LONGITUD_MAXIMA])

    def test_max_length_nss(self):
        self.data['nss'] = '4834 sjdhjsahdkjsajdashdjasdjkhajkdhkjashdjkhasjdhsjvjakdvnsvmn,mnsx'
        form = DatosPersonalesForm(
            self.data
        )
        self.assertEquals(form.errors['nss'], [LONGITUD_MAXIMA])

    def test_max_length_domicilio(self):
        self.data['domicilio'] = 'Jose Ma. Coss #26 hduashdaksjdkcfnsvjbahgfywuyigweyoghiqowUYDUFVGHUFQWASUJKAGHHDFS<JDUFASYGJDHFAVDBHCZXBHJGSVSAHCBJCSSAFAGSYWSCBKJZFCNBHJVSDBCHJVHSBAHDHSAFHAGS'
        form = DatosPersonalesForm(
            self.data
        )
        self.assertEquals(form.errors['domicilio'], [LONGITUD_MAXIMA])

class DatosLaboralesFormTest(TestCase):
    def setUp(self, datos_personales='', matricula_docente='', matricula_nomina='', fecha_ingreso='', no_expediente='', exclusivo='', observaciones_exc='', cvu='', cuerpo_academico='', observaciones_c_a='', programa=''):
        self.data = {
            'datos_personales': datos_personales,
            'matricula_docente': matricula_docente,
            'matricula_nomina': matricula_nomina,
            'fecha_ingreso': fecha_ingreso,
            'no_expediente': no_expediente,
            'exclusivo': exclusivo,
            'observaciones_exc': observaciones_exc,
            'cvu': cvu,
            'cuerpo_academico': cuerpo_academico,
            'observaciones_c_a': observaciones_c_a,
            'programa': programa,
        }

class GradosAcademicosFormTest(TestCase):
    def setUp(self, datos_personales='', escuela='', fecha_obtencion='', categoria_grados='', nombre_estudio='', cedula='', imagen_grado=''):
        self.data = {
            'docente': datos_personales,
            'escuela': escuela,
            'fecha_obtencion': fecha_obtencion,
            'categoria_grados': categoria_grados,
            'nombre_estudio': nombre_estudio,
            'cedula': cedula,
            'imagen_grado': imagen_grado,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['docente'] = 'Viridiana'
        self.data['escuela'] = 'IPN'
        self.data['fecha_obtencion'] = '2017-45-38'
        self.data['categoria_grados'] = 'MAESTRÍA'
        self.data['nombre_estudio'] = 'CIENCIAS SOCIALES'
        self.data['cedula'] = '11234567891568'
        self.data['imagen_grado'] = 'D:\Pictures\Diseños finales\Mtn.jpg'
        form = GradosAcademicosForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_max_length_cedula(self):
        self.data['cedula'] = '123456789102255'
        form = GradosAcademicosForm(
            self.data
        )
        self.assertEquals(form.errors['cedula'], [LONGITUD_MAXIMA])

    def test_max_length_nombre_estudio(self):
        self.data['nombre_estudio'] = 'CIENCIAS SOCIALES DSGGFHBGDCHFDDHGSVSAHCBJCSSAFAGSYWSCBKJZFCNBHJVSDBCHJVHSBAHDHSAFHAGSHGFHDFHFDHDHFHDFH'
        form = GradosAcademicosForm(
            self.data
        )
        self.assertEquals(form.errors['nombre_estudio'], [LONGITUD_MAXIMA])

    def test_grados_academicos_imagen_valida(self):
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
        escuela = Escuela.objects.create(nombre='IPN', clave='4152212')
        img_grado = GradosAcademicos.objects.create(
            docente=datos_personales,
            escuela=escuela,
            fecha_obtencion='2018-06-25',
            categoria_grados='MAESTRÍA',
            nombre_estudio='HISTORIA UNIVERSAL',
            cedula='155515',
            imagen_grado='D:\\Pictures\\pikachu.jpg'
        )
        self.assertEqual(len(GradosAcademicos.objects.all()), 1)

    def test_grados_academicos_imagen_invalida(self):
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
        escuela = Escuela.objects.create(nombre='IPN', clave='4152212')
        img_grado = GradosAcademicos.objects.create(
            docente=datos_personales,
            escuela=escuela,
            fecha_obtencion='2018-06-25',
            categoria_grados='MAESTRÍA',
            nombre_estudio='HISTORIA UNIVERSAL',
            cedula='155515',
            imagen_grado='D://Pictures//pikachu.jpg'
        )

        form = GradosAcademicosForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_grados_academicos_imagen_vacio(self):
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
        escuela = Escuela.objects.create(nombre='IPN', clave='4152212')
        grados_ac = GradosAcademicos.objects.create(
            docente=datos_personales,
            escuela=escuela,
            fecha_obtencion='2018-06-25',
            categoria_grados='MAESTRÍA',
            nombre_estudio='HISTORIA UNIVERSAL',
            cedula='155515'
        )

        form = GradosAcademicosForm(
            data={
                'imagen_grado': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_grados_academicos_nombre_estudio_vacio(self):
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
        escuela = Escuela.objects.create(nombre='IPN', clave='4152212')
        grados_ac = GradosAcademicos.objects.create(
            docente=datos_personales,
            escuela=escuela,
            fecha_obtencion='2018-06-25',
            categoria_grados='MAESTRÍA',
            nombre_estudio='HISTORIA UNIVERSAL',
            cedula='155515',
            imagen_grado='D:\Pictures\Diseños finales\Mtn.jpg'
        )

        form = GradosAcademicosForm(
            data={
                'nombre_estudio': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_grados_academicos_categoria_grados_vacio(self):
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
        escuela = Escuela.objects.create(nombre='IPN', clave='4152212')
        grados_ac = GradosAcademicos.objects.create(
            docente=datos_personales,
            escuela=escuela,
            fecha_obtencion='2018-06-25',
            nombre_estudio='HISTORIA UNIVERSAL',
            cedula='155515',
            imagen_grado='D:\Pictures\Diseños finales\Mtn.jpg'
        )

        form = GradosAcademicosForm(
            data={
                'categoria_grados': '',
            }
        )
        self.assertFalse(form.is_valid())

class ConacytFormTest(TestCase):
    def setUp(self, datos_personales='', numero_proyecto='', nombre_proyecto='', fecha_inicio='', fecha_fin=''):
        self.data = {
            'docente': datos_personales,
            'numero_proyecto': numero_proyecto,
            'nombre_proyecto': nombre_proyecto,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin
        }

    '''def test_si_el_formulario_es_invalido(self):
        self.data['docente'] = 'Viridiana'
        self.data['numero_proyecto'] = '141221'
        self.data['nombre_proyecto'] = 'descripcion'
        self.data['fecha_inicio'] = '2017-36-99'
        self.data['fecha_fin'] = 'CIENCIAS SOCIALES'
        form = ConacytForm(
            self.data
        )
        self.assertFalse(form.is_valid())'''

    def test_max_length_numero_proyecto(self):
        self.data['numero_proyecto'] = '15155151651615615616516'
        form = ConacytForm(
            self.data
        )
        self.assertEquals(form.errors['numero_proyecto'], [LONGITUD_MAXIMA])

    def test_max_length_nombre(self):
        self.data['nombre_proyecto'] = 'JIAPAZ DJSNFKJNGJKSDNVJKDSNKDSNBJDSNJGNJKDSGBDSBGHBGHVBKBSJKSDJKVNJSDSFNJKDNJSDBJSBJSDBJBSDJBGJSFBVGJSDB'
        form = ConacytForm(
            self.data
        )
        self.assertEquals(form.errors['nombre_proyecto'], [LONGITUD_MAXIMA])

    # def test_numero_proyecto_vacio(self):
    #     estado = Estado.objects.create(
    #         nombre='Zacatecas'
    #     )
    #     municipio = Municipio.objects.create(
    #         estado=estado,
    #         nombre='Guadalupe'
    #     )
    #     datos_personales = DatosPersonales.objects.create(
    #         nombres='Viridiana',
    #         ap_paterno='Gutiérrez',
    #         ap_materno='Villalobos',
    #         fecha_nacimiento='1997-02-11',
    #         rfc='GUVM970211HU7',
    #         curp='GUVM970211MSTLT09',
    #         nss='4834',
    #         domicilio='Jose Ma. Coss #26',
    #         municipio=municipio,
    #         status=True
    #     )
    #     conacyt = Conacyt.objects.create(
    #         docente=datos_personales,
    #         nombre_proyecto='JIAPAZ',
    #         fecha_inicio_conacyt='2017-08-21',
    #         fecha_fin_conacyt='2018-01-30'
    #     )
    #
    #     form = ConacytForm(
    #         data={
    #             'numero_proyecto': '',
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_nombre_proyecto_vacio(self):
    #     estado = Estado.objects.create(
    #         nombre='Zacatecas'
    #     )
    #     municipio = Municipio.objects.create(
    #         estado=estado,
    #         nombre='Guadalupe'
    #     )
    #     datos_personales = DatosPersonales.objects.create(
    #         nombres='Viridiana',
    #         ap_paterno='Gutiérrez',
    #         ap_materno='Villalobos',
    #         fecha_nacimiento='1997-02-11',
    #         rfc='GUVM970211HU7',
    #         curp='GUVM970211MSTLT09',
    #         nss='4834',
    #         domicilio='Jose Ma. Coss #26',
    #         municipio=municipio,
    #         status=True
    #     )
    #     conacyt = Conacyt.objects.create(
    #         docente=datos_personales,
    #         numero_proyecto='154154',
    #         fecha_inicio_conacyt='2017-08-21',
    #         fecha_fin_conacyt='2018-01-30'
    #     )
    #
    #     form = ConacytForm(
    #         data={
    #             'nombre_proyecto': '',
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

class ProdepFormTest(TestCase):
    def setUp(self, datos_personales='', clave='', descripcion='', fecha_inicio='', fecha_fin='', imagen_prodep=''):
        self.data = {
            'docente': datos_personales,
            'clave': clave,
            'descripcion': descripcion,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'imagen_prodep': imagen_prodep
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['docente'] = 'Viridiana'
        self.data['clave'] = '141221'
        self.data['descripcion'] = 'descripcion'
        self.data['fecha_inicio'] = '2017-36-99'
        self.data['fecha_fin'] = 'CIENCIAS SOCIALES'
        self.data['imagen_prodep'] = 'D:\Pictures\Diseños finales\Mtn.jpg'
        form = ProdepForm(
            self.data
        )
        self.assertTrue(form.is_valid())

    def test_prodep_imagen_valida(self):
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
        prodep = Prodep.objects.create(
            docente=datos_personales,
            clave='216515',
            descripcion='descripcion',
            fecha_inicio_prodep='2017-06-25',
            fecha_fin_prodep='2017-11-25',
            imagen_prodep='D:\\Pictures\\pikachu.jpg'
        )
        self.assertEqual(len(Prodep.objects.all()), 1)

    # def test_prodep_imagen_invalida(self):
    #     estado = Estado.objects.create(
    #         nombre='Zacatecas'
    #     )
    #     municipio = Municipio.objects.create(
    #         estado=estado,
    #         nombre='Guadalupe'
    #     )
    #     datos_personales = DatosPersonales.objects.create(
    #         nombres='Viridiana',
    #         ap_paterno='Gutiérrez',
    #         ap_materno='Villalobos',
    #         fecha_nacimiento='1997-02-11',
    #         rfc='GUVM970211HU7',
    #         curp='GUVM970211MSTLT09',
    #         nss='4834',
    #         domicilio='Jose Ma. Coss #26',
    #         municipio=municipio,
    #         status=True
    #     )
    #     prodep = Prodep.objects.create(
    #         docente=datos_personales,
    #         clave='216515',
    #         descripcion='descripcion',
    #         fecha_inicio_prodep='2017-06-25',
    #         fecha_fin_prodep='2017-11-25',
    #         imagen_prodep='D:\\Pictures\\pikachu.jpg'
    #     )
    #
    #     form = ProdepForm(
    #         self.data
    #     )
    #     self.assertFalse(form.is_valid())

    def test_max_length_clave(self):
        self.data['clave'] = '15155151651615615616516'
        form = ProdepForm(
            self.data
        )
        self.assertEquals(form.errors['clave'], [LONGITUD_MAXIMA])

    # def test_prodep_imagen_vacio(self):
    #     estado = Estado.objects.create(
    #         nombre='Zacatecas'
    #     )
    #     municipio = Municipio.objects.create(
    #         estado=estado,
    #         nombre='Guadalupe'
    #     )
    #     datos_personales = DatosPersonales.objects.create(
    #         nombres='Viridiana',
    #         ap_paterno='Gutiérrez',
    #         ap_materno='Villalobos',
    #         fecha_nacimiento='1997-02-11',
    #         rfc='GUVM970211HU7',
    #         curp='GUVM970211MSTLT09',
    #         nss='4834',
    #         domicilio='Jose Ma. Coss #26',
    #         municipio=municipio,
    #         status=True
    #     )
    #     prodep = Prodep.objects.create(
    #         docente=datos_personales,
    #         clave='216515',
    #         descripcion='descripcion',
    #         fecha_inicio_prodep='2017-06-25',
    #         fecha_fin_prodep='2017-11-25'
    #     )
    #     form = ProdepForm(
    #         data={
    #             'imagen_prodep': '',
    #         }
    #     )
    #     self.assertFalse(form.is_valid())
    #
    # def test_prodep_clave_vacio(self):
    #     estado = Estado.objects.create(
    #         nombre='Zacatecas'
    #     )
    #     municipio = Municipio.objects.create(
    #         estado=estado,
    #         nombre='Guadalupe'
    #     )
    #     datos_personales = DatosPersonales.objects.create(
    #         nombres='Viridiana',
    #         ap_paterno='Gutiérrez',
    #         ap_materno='Villalobos',
    #         fecha_nacimiento='1997-02-11',
    #         rfc='GUVM970211HU7',
    #         curp='GUVM970211MSTLT09',
    #         nss='4834',
    #         domicilio='Jose Ma. Coss #26',
    #         municipio=municipio,
    #         status=True
    #     )
    #     prodep = Prodep.objects.create(
    #         docente=datos_personales,
    #         descripcion='descripcion',
    #         fecha_inicio_prodep='2017-06-25',
    #         fecha_fin_prodep='2017-11-25',
    #         imagen_prodep='D:\Pictures\Diseños finales\Mtn.jpg'
    #     )
    #     form = ProdepForm(
    #         data={
    #             'clave': '',
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

class SniFormTest(TestCase):
    def setUp(self, datos_personales='', clave='', descripcion='', fecha_inicio='', fecha_fin='', nivel='', imagen_sni=''):
        self.data = {
            'docente': datos_personales,
            'clave': clave,
            'descripcion': descripcion,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'nivel': nivel,
            'imagen_sni': imagen_sni
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['docente'] = 'Viridiana'
        self.data['clave'] = '141221'
        self.data['descripcion'] = 'descripcion'
        self.data['fecha_inicio'] = '2017-36-99'
        self.data['fecha_fin'] = 'CIENCIAS SOCIALES'
        self.data['nivel'] = 'NIVEL'
        self.data['imagen_sni'] = 'D:\Pictures\Diseños finales\Mtn.jpg'
        form = SniForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_max_length_clave(self):
        self.data['clave'] = '15155151651615615616516'
        form = ProdepForm(
            self.data
        )
        self.assertEquals(form.errors['clave'], [LONGITUD_MAXIMA])

    def test_prodep_imagen_valida(self):
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
        sni = Sni.objects.create(
            docente=datos_personales,
            clave='216515',
            descripcion='descripcion',
            fecha_inicio_sni='2017-06-25',
            fecha_fin_sni='2017-11-25',
            imagen_sni='D:\\Pictures\\pikachu.jpg'
        )
        self.assertEqual(len(Sni.objects.all()), 1)

class CategoriaIncidenciasFormTest(TestCase):
    def setUp(self, permiso='', clausula=''):
        self.data = {
            'permiso': permiso,
            'clausula': clausula,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['permiso'] = '254545454'
        self.data['clausula'] = 'safafsaf'
        form = CategoriaIncidenciasForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_max_length_permiso(self):
        self.data['permiso'] = 'Permiso economico jrfijlmcdslv,dl,amskcn jbxqfwdtyefwyvhklfbmvdfmvdbcbhasghjgvkjdankvacsajkbchjasvhjbdvjkbasjkbcjsanc ndvbfnsvjabsjvkcbakcbaksjbcjkasbckabsckj'
        form = CategoriaIncidenciasForm(
            self.data
        )
        self.assertEquals(form.errors['permiso'], [LONGITUD_MAXIMA])

    def test_categoria_incidencias_permiso_vacio(self):
        cat_incidencias = CategoriaIncidencias.objects.create(
            clausula=1323262
        )
        form = CategoriaIncidenciasForm(
            data={
                'permiso': '',
            }
        )
        self.assertFalse(form.is_valid())

class CategoriaGradosFormTest(TestCase):
    def setUp(self, nombre='', desc=''):
        self.data = {
            'nombre': nombre,
            'desc': desc,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['nombre'] = '254545454'
        self.data['desc'] = '13131311'
        form = CategoriaGradosForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_max_length_desc(self):
        self.data['desc'] = 'Permiso economico jrfijlmcdslv,dl,amskcn jbxqfwdtyefwyvhklfbmvdfmvdbcbhasghjgvkjdankvacsajkbchjasvhjbdvjkbasjkbcjsanc ndvbfnsvjabsjvkcbakcbaksjbcjkasbckabsckj'
        form = CategoriaGradosForm(
            self.data
        )
        self.assertEquals(form.errors['desc'], [LONGITUD_MAXIMA])

    def test_categoria_grados_nombre_vacio(self):
        cat_grados = CategoriaGrados.objects.create(
            desc='Aquí va la descripción'
        )
        form = CategoriaGradosForm(
            data={
                'nombre': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_categoria_grados_desc_vacio(self):
        cat_grados = CategoriaGrados.objects.create(
            nombre='Lincenciatura'
        )
        form = CategoriaGradosForm(
            data={
                'desc': '',
            }
        )
        self.assertFalse(form.is_valid())

class EscuelaFormTest(TestCase):
    def setUp(self, nombre='', clave=''):
        self.data = {
            'nombre': nombre,
            'clave': clave,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['nombre'] = '254545454'
        self.data['clave'] = '1321313131213213221'
        form = EscuelaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_si_el_formulario_es_valido(self):
        self.data['nombre'] = 'Universidad Autónoma de Zacatecas'
        self.data['clave'] = '132131'
        form = EscuelaForm(
            self.data
        )
        self.assertTrue(form.is_valid())

    def test_max_length_nombre_escuela(self):
        self.data['nombre'] = 'Universidad Autónoma de Zacatecas jrfijlmcdslv,dl,amskcn jbxqfwdtyefwyvhklfbmvdfmvdbcbhasghjgvkjdankvacsajkbchjasvhjbdvjkbasjkbcjsanc ndvbfnsvjabsjvkcbakcbaksjbcjkasbckabsckj'
        form = EscuelaForm(
            self.data
        )
        self.assertEquals(form.errors['nombre'], [LONGITUD_MAXIMA])

    def test_escuela_nombre_vacio(self):
        escuela = Escuela.objects.create(
            clave=25262
        )
        form = EscuelaForm(
            data={
                'nombre': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_escuela_clave_vacio(self):
        escuela = Escuela.objects.create(
            nombre='Universidad Autónoma de Zacatecas'
        )
        form = EscuelaForm(
            data={
                'clave': '',
            }
        )
        self.assertFalse(form.is_valid())

class UnidadAcademicaFormTest(TestCase):
    def setUp(self, clave_nueva='', clave_antigua='', nombre=''):
        self.data = {
            'clave_nueva': clave_nueva,
            'clave_antigua': clave_antigua,
            'nombre': nombre,

        }

    def test_si_el_formulario_es_invalido(self):
        self.data['clave_nueva'] = '1321313131213213221'
        self.data['clave_antigua'] = '1321313131213213221'
        self.data['nombre'] = '254545454'
        form = UnidadAcademicaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_si_el_formulario_es_valido(self):
        self.data['clave_nueva'] = '2222'
        self.data['clave_antigua'] = '545'
        self.data['nombre'] = 'Ingeniería Eléctrica'
        form = UnidadAcademicaForm(
            self.data
        )
        self.assertTrue(form.is_valid())

    def test_max_length_nombre(self):
        self.data['nombre'] = 'Ingeniería Eléctrica jrfijlmcdslv,dl,amskcn jbxqfwdtyefwyvhklfbmvdfmvdbcbhasghjgvkjdankvacsajkbchjasvhjbdvjk'
        form = UnidadAcademicaForm(
            self.data
        )
        self.assertEquals(form.errors['nombre'], [LONGITUD_MAXIMA])

    def test_unidad_nombre_vacio(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=25262,
            clave_antigua=54545,
        )
        form = UnidadAcademicaForm(
            data={
                'nombre': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_unidad_clave_nueva_vacia(self):
        unidad = UnidadAcademica.objects.create(
            clave_antigua=54545,
            nombre='Ingeniería Eléctrica'
        )
        form = UnidadAcademicaForm(
            data={
                'clave_nueva': '',
            }
        )
        self.assertFalse(form.is_valid())

class ProgramaFormTest(TestCase):
    def setUp(self, programa='', unidad_academica=''):
        self.data = {
            'programa': programa,
            'unidad_academica': unidad_academica,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['programa'] = '1321313131213213221'
        self.data['unidad_academica'] = '1321313131213213221'
        form = ProgramaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_si_el_formulario_es_valido(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=25262,
            clave_antigua=54545,
            nombre='Ingeniería Eléctrica'
        )
        programa = Programa.objects.create(
            programa='Ingeniería de Software',
            unidad_academica=unidad)
        self.data['programa'] = programa
        self.data['unidad_academica'] = unidad
        form = ProgramaForm(
            self.data
        )
        self.assertTrue(form.is_valid())

    def test_max_length_nombre_programa(self):
        self.data['programa'] = 'Ingeniería Eléctrica jrfijlmcdslv,dl,amskcn jbxqfwdtyefwyvhklfbmvdfmvdbcbhasghjgvkjdankvacsajkbchjasvhjbdvjk'
        form = ProgramaForm(
            self.data
        )
        self.assertEquals(form.errors['programa'], [LONGITUD_MAXIMA])

    def test_programa_nombre_vacio(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=25262,
            clave_antigua=54545,
            nombre='Ingeniería Eléctrica'
        )
        programa = Programa.objects.create(
            unidad_academica=unidad)
        form = ProgramaForm(
            data={
                'programa': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_programa_unidad_academica_vacia(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=223,
            clave_antigua=252,
            nombre='Ingeniería Eléctrica'
        )
        programa = Programa.objects.create(programa='Ingeniería de Software',
                                           unidad_academica=unidad)
        form = ProgramaForm(
            data={
                'unidad_academica': None,
            }
        )
        self.assertFalse(form.is_valid())

class MateriaFormTest(TestCase):
    def setUp(self, nombre='', clave='', semestre='', programa=''):
        self.data = {
            'nombre': nombre,
            'clave': clave,
            'semestre': semestre,
            'programa': programa,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['nombre'] = '1321313131213213221'
        self.data['clave'] = '132131313121321322188809090098089809080808'
        self.data['semestre'] = '2018-03-25'
        self.data['programa'] = '1321313131213213221'
        form = MateriaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_si_el_formulario_es_valido(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=25262,
            clave_antigua=54545,
            nombre='Ingeniería Eléctrica'
        )
        programa = Programa.objects.create(
            programa='Ingeniería de Software',
            unidad_academica=unidad)
        materia = Materia.objects.create(
            nombre='Ecuaciones Diferenciales',
            clave=255,
            semestre=5,
            programa=programa
        )
        self.data['nombre'] = materia
        self.data['clave'] = 1313
        self.data['semestre'] = 5
        self.data['programa'] = programa
        form = MateriaForm(
            self.data
        )
        self.assertTrue(form.is_valid())

    def test_max_length_nombre_materia(self):
        self.data['nombre'] = 'Ecuaciones Diferenciales jrfijlmcdslv,dl,amskcn jbxqfwdtyefwyvhklfbmvdfmvdbcbhasghjgvkjdankvacsajkbchjasvhjbdvjk'
        form = MateriaForm(
            self.data
        )
        self.assertEquals(form.errors['nombre'], [LONGITUD_MAXIMA])

    def test_materia_nombre_vacio(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=25262,
            clave_antigua=54545,
            nombre='Ingeniería Eléctrica'
        )
        programa = Programa.objects.create(
                programa='Ingeniería de Software',
                unidad_academica=unidad)
        materia = Materia.objects.create(
                clave=255,
                semestre=5,
                programa=programa
        )
        form = MateriaForm(
            data={
                'nombre': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_programa_vacio(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=223,
            clave_antigua=252,
            nombre='Ingeniería Eléctrica'
        )
        programa = Programa.objects.create(programa='Ingeniería de Software',
                                           unidad_academica=unidad)
        materia = Materia.objects.create(
            nombre='Ecuaciones Diferenciales',
            clave=255,
            semestre=5,
            programa=programa
        )
        form = MateriaForm(
            data={
                'programa': None,
            }
        )
        self.assertFalse(form.is_valid())

class CuerpoAcademicoFormTest(TestCase):
    def setUp(self, no_registro='', nombre='', unidad_academica='', fecha_inicio='', fecha_fin=''):
        self.data = {
            'no_registro': no_registro,
            'nombre': nombre,
            'unidad_academica': unidad_academica,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['no_registro'] = '132131313121321322188809090098089809080808'
        self.data['nombre'] = '1321313131213213221'
        self.data['unidad_academica'] = '9809080808'
        self.data['fecha_inicio'] = '2018-30-80'
        self.data['fecha_fin'] = '1321313131213213221'
        form = MateriaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_si_el_formulario_es_valido(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=25262,
            clave_antigua=54545,
            nombre='Ingeniería Eléctrica'
        )
        cuerpo_ac = CuerpoAcademico.objects.create(
            no_registro='1211',
            nombre='Cuerpo Academico',
            unidad_academica=unidad,
            fecha_inicio='2018-05-30',
            fecha_fin='2019-05-20'
        )

        self.data['no_registro'] = '44414'
        self.data['nombre'] = 'Cuerpo Académico'
        self.data['unidad_academica'] = unidad
        self.data['fecha_inicio'] = '2018-05-30'
        self.data['fecha_fin'] = '2019-05-20'
        form = CuerpoAcademicoForm(
            self.data
        )
        self.assertTrue(form.is_valid())

    def test_max_length_nombre_cuerpo_academico(self):
        self.data['nombre'] = 'Ecuaciones Diferenciales jrfijlmcdslv,dl,amskcn jbxqfwdtyefwyvhklfbmvdfmvdbcbhasghjgvkjdankvacsajkbchjasvhjbdvjk'
        form = CuerpoAcademicoForm(
            self.data
        )
        self.assertEquals(form.errors['nombre'], [LONGITUD_MAXIMA])

    def test_max_length_no_registro_cuerpo_academico(self):
        self.data['no_registro'] = 'Ecuaciones Diferenciales jrfijlmcdslv,dl,amskcn jbxqfwdtyefwyvhklfbmvdfmvdbcbhasghjgvkjdankvacsajkbchjasvhjbdvjk'
        form = CuerpoAcademicoForm(
            self.data
        )
        self.assertEquals(form.errors['no_registro'], [LONGITUD_MAXIMA])

    def test_cuerpo_academico_nombre_vacio(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=25262,
            clave_antigua=54545,
            nombre='Ingeniería Eléctrica'
        )
        cuerpo_ac = CuerpoAcademico.objects.create(
                no_registro='551515',
                unidad_academica=unidad,
                fecha_inicio='2018-05-30',
                fecha_fin='2019-05-20'
        )
        form = CuerpoAcademicoForm(
            data={
                'nombre': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_cuerpo_academico_no_registro_vacio(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=25262,
            clave_antigua=54545,
            nombre='Ingeniería Eléctrica'
        )
        cuerpo_ac = CuerpoAcademico.objects.create(
                nombre='Cuerpo Academico',
                unidad_academica=unidad,
                fecha_inicio='2018-05-30',
                fecha_fin='2019-05-20'
        )
        form = CuerpoAcademicoForm(
            data={
                'no_registro': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_unidad_academica_vacio(self):
        unidad = UnidadAcademica.objects.create(
            clave_nueva=223,
            clave_antigua=252,
            nombre='Ingeniería Eléctrica'
        )
        cuerpo_ac = CuerpoAcademico.objects.create(
            no_registro='1211',
            nombre='Cuerpo Academico',
            unidad_academica=unidad,
            fecha_inicio='2018-05-30',
            fecha_fin='2019-05-20'
        )
        form = CuerpoAcademicoForm(
            data={
                'unidad_academica': None,
            }
        )
        self.assertFalse(form.is_valid())