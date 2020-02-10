from django.test import TestCase
from django.urls import reverse

from apps.docente.models import DatosPersonales, DatosLaborales, Estado, Municipio
from apps.nivel.models import Nivel, Oficio, Bandera, Codificacion
from apps.docente.forms import DatosPersonalesForm


class NivelViewTest(TestCase):

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
        self.datos_laborales = DatosLaborales.objects.create(
            datos_personales=self.datos_personales,
            matricula_docente='1234',
            matricula_nomina='123345',
            fecha_ingreso='2012-12-12',
            no_expediente=123.12,
            exclusivo=False,
            cuerpo_academico=None
        )

        self.oficio = Oficio.objects.create(
            numero=312,
            emisor='COMISION MIXTA',
            fecha_oficio='2019-12-12',
            imagen_oficios='oficios/oficio1.jpg'
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

        self.nivel = Nivel.objects.create(
            datos_personales=self.datos_personales,
            oficio=self.oficio,
            fecha_movimiento='2019-10-08',
            via='REQUISITOS',
            bandera=self.bandera,
            cod_nivel=self.codificacion,
            observaciones='no tengo ninguna observación de esto'
        )

    def test_url_lista_nivel(self):
        response = self.client.get('/nivel/listar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nivel/lista_niveles.html')

    def test_url_nuevo_nivel(self):
        response = self.client.get('/nivel/niveles/nuevo/1')
        self.assertEqual(response.status_code, 200)

    def test_template_nuevo_nivel(self):
        response = self.client.get('/nivel/niveles/nuevo/1')
        self.assertTemplateUsed(response, 'nivel/nivel_form.html')

    # def test_url_detalles_docente(self):
    #     response = self.client.get('/docente/detalles/1')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'docente/docente_detalles.html')
    #
    # def test_cambiar_estatus_docente_inactivo(self):
    #     response = self.client.get(f'/docente/activar/{self.datos_personales.id}')
    #     nuevo_docente = DatosPersonales.objects.first()
    #     self.assertEqual(nuevo_docente.status, False)
    #     response = self.client.get(f'/docente/activar/{self.datos_personales.id}')
    #     mismo_docente = DatosPersonales.objects.first()
    #     self.assertEqual(nuevo_docente.status, True)
    #
    # def test_envio_datos_docente(self):
    #     response = self.client.get('/docente/listar')
    #     self.assertIn('object_list', response.context)

# class DocenteNuevoTest(TestCase):
#
#     def setUp(self):
#         estado = Estado.objects.create(
#             nombre='Zacatecas'
#         )
#         municipio = Municipio.objects.create(
#             estado=estado,
#             nombre='Zacatecas'
#         )
#         self.datos_personales = DatosPersonales.objects.create(
#             nombres='Pedro',
#             ap_paterno='Sánchez',
#             ap_materno='Hinostroza',
#             fecha_nacimiento='1999-10-07',
#             rfc='SAHP981007KF7',
#             curp='SAHP981007HZSNND03',
#             nss='3124',
#             sexo='HOMBRE',
#             estado_civil='SOLTERO',
#             domicilio='Priv. Caleros 116',
#             municipio=municipio,
#             status=True
#         )
#         self.datos_laborales = DatosLaborales.objects.create(
#             datos_personales=self.datos_personales,
#             matricula_docente='1234',
#             matricula_nomina='123345',
#             fecha_ingreso='2012-12-12',
#             no_expediente=123.12,
#             exclusivo=False,
#             cuerpo_academico=None
#         )
#
#         self.data = {
#             'nombres': self.datos_personales.nombres,
#             'ap_paterno': self.datos_personales.ap_paterno,
#             'ap_materno': self.datos_personales.ap_materno,
#             'fecha_nacimiento': self.datos_personales.fecha_nacimiento,
#             'rfc': self.datos_personales.rfc,
#             'curp': self.datos_personales.curp,
#             'nss': self.datos_personales.nss,
#             'sexo': self.datos_personales.sexo,
#             'estado_civil': self.datos_personales.estado_civil,
#             'domicilio': self.datos_personales.domicilio,
#             'municipio': self.datos_personales.municipio,
#             'matricula_docente': self.datos_laborales.matricula_docente,
#             'matricula_nomina': self.datos_laborales.matricula_nomina,
#             'fecha_ingreso': self.datos_laborales.fecha_ingreso,
#             'no_expediente': self.datos_laborales.no_expediente
#         }
#
#
#
#     def test_url_nuevo_docente(self):
#         response = self.client.get('/docente/nuevo')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'docente/docente_nuevo.html')
#
#     def test_puede_guardar_peticiones_post(self):
#         self.assertEqual(DatosPersonales.objects.count(), 1)
#         nuevo_docente = DatosPersonales.objects.first()
#         self.assertEqual(nuevo_docente.nombres, self.datos_personales.nombres)
#
#     # def test_redirecciona_despues_de_POST(self):
#     #     response = self.client.post('/docente/nuevo', self.data)
#     #     self.assertRedirects(response, '/docente/listar')
#
#     def test_entrada_invalida_en_template_con_formulario(self):
#         response = self.client.post('/docente/nuevo', data={'nombres': ''})
#         self.assertIsInstance(response.context['personales'], DatosPersonalesForm)
#
#     def test_docentes_invalidos_no_se_guardan(self):
#         self.client.post('/docente/nuevo', data={'nombres': ''})
#         # El 1 es para ver que no guardó el de la línea de arriba
#         self.assertEqual(DatosPersonales.objects.count(), 1)
#
# class GradoAcademicoNuevoTest(TestCase):
#
#     def setUp(self):
#         estado = Estado.objects.create(
#             nombre='Zacatecas'
#         )
#         municipio = Municipio.objects.create(
#             estado=estado,
#             nombre='Zacatecas'
#         )
#         self.datos_personales = DatosPersonales.objects.create(
#             nombres='Pedro',
#             ap_paterno='Sánchez',
#             ap_materno='Hinostroza',
#             fecha_nacimiento='1999-10-07',
#             rfc='SAHP981007KF7',
#             curp='SAHP981007HZSNND03',
#             nss='3124',
#             sexo='HOMBRE',
#             estado_civil='SOLTERO',
#             domicilio='Priv. Caleros 116',
#             municipio=municipio,
#             status=True
#         )
#         self.datos_laborales = DatosLaborales.objects.create(
#             datos_personales=self.datos_personales,
#             matricula_docente='1234',
#             matricula_nomina='123345',
#             fecha_ingreso='2012-12-12',
#             no_expediente=123.12,
#             exclusivo=False,
#             cuerpo_academico=None
#         )
#
#         self.escuela = Escuela.objects.create(
#             nombre='UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO',
#             clave='213412'
#         )
#
#         self.grado_academico = GradosAcademicos.objects.create(
#             docente = self.datos_personales,
#             escuela = self.escuela,
#             fecha_obtencion = '2016-12-12',
#             categoria_grados = 'DOCTORADO',
#             nombre_estudio = 'Ciencias de la TICs',
#             cedula = '2132412',
#             imagen_grado = 'grados_academicos/grado1.jpg'
#         )
#
#         self.data = {
#             'docente' : self.datos_personales,
#             'escuela' : self.escuela,
#             'fecha_obtencion' : '2016-12-12',
#             'categoria_grados' : 'DOCTORADO',
#             'nombre_estudio' : 'Ciencias de la TICs',
#             'cedula' : '2132412',
#             'imagen_grado' : 'grados_academicos/grado1.jpg'
#         }
#
#     def test_url_nuevo_grado_academico(self):
#         response = self.client.get(f'/docente/gradonuevo/{self.datos_personales.id}')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'docente/grado_academico_form.html')
#
#     def test_puede_guardar_peticiones_post_grado_acedemico(self):
#         self.assertEqual(GradosAcademicos.objects.count(), 1)
#         nuevo_grado = GradosAcademicos.objects.first()
#         self.assertEqual(nuevo_grado.nombre_estudio, self.grado_academico.nombre_estudio)
#
#     # def test_redirecciona_despues_de_POST(self):
#     #     response = self.client.post('/docente/gradonuevo', self.data)
#     #     self.assertRedirects(response, '/docente/listar')
#     #
#     # def test_entrada_invalida_en_template_con_formulario_grado_academico(self):
#     #     response = self.client.post(f'/docente/gradonuevo/{self.datos_personales.id}', data={'escuela': ''})
#     #     self.assertIsInstance(response.context['form_grado'], GradosAcademicosForm)
#
#     def test_grados_academicos_invalidos_no_se_guardan(self):
#         self.client.post('/docente/nuevo', data={'nombres': ''})
#         # El 1 es para ver que no guardó el de la línea de arriba
#         self.assertEqual(GradosAcademicos.objects.count(), 1)
