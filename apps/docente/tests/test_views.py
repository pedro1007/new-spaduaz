from django.test import TestCase
from apps.docente.models import DatosPersonales, DatosLaborales, Estado, Municipio, GradosAcademicos, Escuela, CategoriaIncidencias, CategoriaGrados, Escuela, UnidadAcademica, Programa, Materia, CuerpoAcademico
from apps.docente.forms import DatosPersonalesForm, GradosAcademicosForm, CategoriaIncidenciasForm, EscuelaForm, UnidadAcademicaForm, ProgramaForm, MateriaForm, CuerpoAcademicoForm

class DocenteViewTest(TestCase):

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

    def test_url_lista_docentes(self):
        response = self.client.get('/docente/listar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'docente/lista_docente.html')

    def test_url_detalles_docente(self):
        response = self.client.get('/docente/detalles/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'docente/docente_detalles.html')

    def test_cambiar_estatus_docente_inactivo_y_activo(self):
        response = self.client.get(f'/docente/activar/{self.datos_personales.id}')
        nuevo_docente = DatosPersonales.objects.first()
        self.assertEqual(nuevo_docente.status, False)
        response = self.client.get(f'/docente/activar/{self.datos_personales.id}')
        mismo_docente = DatosPersonales.objects.first()
        self.assertEqual(mismo_docente.status, True)

    def test_envio_datos_docente(self):
        response = self.client.get('/docente/listar')
        self.assertIn('object_list', response.context)

class DocenteNuevoTest(TestCase):

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

    def test_puede_guardar_peticiones_post(self):
        self.assertEqual(DatosPersonales.objects.count(), 1)
        nuevo_docente = DatosPersonales.objects.first()
        self.assertEqual(nuevo_docente.nombres, self.datos_personales.nombres)

    def test_docentes_invalidos_no_se_guardan(self):
        self.client.post('/docente/nuevo', data={'nombres': ''})
        # El 1 es para ver que no guardó el de la línea de arriba
        self.assertEqual(DatosPersonales.objects.count(), 1)

class GradoAcademicoNuevoTest(TestCase):

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

        self.escuela = Escuela.objects.create(
            nombre='UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO',
            clave='213412'
        )

        self.grado_academico = GradosAcademicos.objects.create(
            docente = self.datos_personales,
            escuela = self.escuela,
            fecha_obtencion = '2016-12-12',
            categoria_grados = 'DOCTORADO',
            nombre_estudio = 'Ciencias de la TICs',
            cedula = '2132412',
            imagen_grado = 'grados_academicos/grado1.jpg'
        )

    def test_url_nuevo_grado_academico(self):
        response = self.client.get(f'/docente/gradonuevo/{self.datos_personales.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'docente/grado_academico_form.html')

    def test_puede_guardar_peticiones_post_grado_acedemico(self):
        self.assertEqual(GradosAcademicos.objects.count(), 1)
        nuevo_grado = GradosAcademicos.objects.first()
        self.assertEqual(nuevo_grado.nombre_estudio, self.grado_academico.nombre_estudio)

    def test_grados_academicos_invalidos_no_se_guardan(self):
        self.client.post('/docente/nuevo', data={'nombres': ''})
        # El 1 es para ver que no guardó el de la línea de arriba
        self.assertEqual(GradosAcademicos.objects.count(), 1)

class CatIncidenciasView(TestCase):

    def test_url_lista_cat_incidencias(self):
        response = self.client.get('/docente/incidencias/listar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/cat_incidencias_list.html')

    def test_envio_datos_cat_incidencia(self):
        response = self.client.get('/docente/incidencias/listar')
        self.assertIn('object_list', response.context)

class CatIncidenciasNueva(TestCase):

    def setUp(self):
        self.cat_incidencia = CategoriaIncidencias.objects.create(
            permiso='Año Sabático',
            clausula=213
        )

    def test_url_nueva_cat_incidencia(self):
        response = self.client.get('/docente/incidencias/agregar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/cat_incidencias_form.html')

    def test_cat_incidencias_puede_guardar_peticiones_post(self):
        self.assertEqual(CategoriaIncidencias.objects.count(), 1)
        nueva_cat_incidencias = CategoriaIncidencias.objects.first()
        self.assertEqual(nueva_cat_incidencias.permiso, self.cat_incidencia.permiso)

    def test_cat_incidencias_invalidos_no_se_guardan(self):
        self.client.post('/docente/incidencias/agregar', data={'clausula': ''})
        # El 1 es para ver que no guardó el de la línea de arriba
        self.assertEqual(CategoriaIncidencias.objects.count(), 1)

class EscuelasView(TestCase):

    def test_url_lista_escuela(self):
        response = self.client.get('/docente/escuelas/listar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/escuelas_list.html')

    def test_envio_datos_escuela(self):
        response = self.client.get('/docente/escuelas/listar')
        self.assertIn('object_list', response.context)

class EscuelaNueva(TestCase):

    def setUp(self):
        self.escuela = Escuela.objects.create(
            nombre='UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO',
            clave='21312'
        )

    def test_url_nueva_escuela(self):
        response = self.client.get('/docente/escuelas/agregar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/escuela_form.html')

    def test_escuela_puede_guardar_peticiones_post(self):
        self.assertEqual(Escuela.objects.count(), 1)
        nueva_escuela = Escuela.objects.first()
        self.assertEqual(nueva_escuela.clave, self.escuela.clave)

    def test_escuela_invalidos_no_se_guardan(self):
        self.client.post('/docente/escuela/agregar', data={'nombre': ''})
        # El 1 es para ver que no guardó el de la línea de arriba
        self.assertEqual(Escuela.objects.count(), 1)

class UnidadAcademicaView(TestCase):

    def test_url_lista_unidad_academica(self):
        response = self.client.get('/docente/unidades/listar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/unidad_academica_list.html')

    def test_envio_datos_unidad_academica(self):
        response = self.client.get('/docente/unidades/listar')
        self.assertIn('object_list', response.context)

class UnidadAcademicaNueva(TestCase):

    def setUp(self):
        self.unidad_academica = UnidadAcademica.objects.create(
            clave_nueva = '123',
            clave_antigua = '312',
            nombre = 'Ingeniería Eléctrica'
        )

    def test_url_nueva_unidad(self):
        response = self.client.get('/docente/unidades/agregar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/unidad_academica_form.html')

    def test_unidad_academica_puede_guardar_peticiones_post(self):
        self.assertEqual(UnidadAcademica.objects.count(), 1)
        nueva_unidad = UnidadAcademica.objects.first()
        self.assertEqual(nueva_unidad.nombre, self.unidad_academica.nombre)

    def test_uniadad_academica_entrada_invalida_en_template_con_formulario(self):
        response = self.client.post('/docente/unidades/agregar', data={'nombre': ''})
        self.assertIsInstance(response.context['form'], UnidadAcademicaForm)

    def test_uniadad_academica_invalidos_no_se_guardan(self):
        self.client.post('/docente/unidades/agregar', data={'nombre': ''})
        # El 1 es para ver que no guardó el de la línea de arriba
        self.assertEqual(UnidadAcademica.objects.count(), 1)

class ProgramaView(TestCase):

    def test_url_lista_programas(self):
        response = self.client.get('/docente/programas/listar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/programa_list.html')

    def test_envio_datos_programas(self):
        response = self.client.get('/docente/programas/listar')
        self.assertIn('object_list', response.context)

class ProgramaNuevo(TestCase):

    def setUp(self):
        self.unidad_academica = UnidadAcademica.objects.create(
            clave_nueva = '123',
            clave_antigua = '312',
            nombre = 'Ingeniería Eléctrica'
        )

        self.programa = Programa.objects.create(
            programa='Ingeniería de Software',
            unidad_academica=self.unidad_academica
        )

    def test_url_nuevo_programa(self):
        response = self.client.get('/docente/programas/agregar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/programa_form.html')

    def test_programa_puede_guardar_peticiones_post(self):
        self.assertEqual(Programa.objects.count(), 1)
        nueva_programa = Programa.objects.first()
        self.assertEqual(nueva_programa.programa, self.programa.programa)

    def test_programa_entrada_invalida_en_template_con_formulario(self):
        response = self.client.post('/docente/programas/agregar', data={'programa': ''})
        self.assertIsInstance(response.context['form'], ProgramaForm)

    def test_programa_invalidos_no_se_guardan(self):
        self.client.post('/docente/programas/agregar', data={'programa': ''})
        # El 1 es para ver que no guardó el de la línea de arriba
        self.assertEqual(Programa.objects.count(), 1)

class MateriaView(TestCase):

    def test_url_lista_materia(self):
        response = self.client.get('/docente/materias/listar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/materias_list.html')

    def test_envio_datos_materia(self):
        response = self.client.get('/docente/materias/listar')
        self.assertIn('object_list', response.context)

class MateriaNueva(TestCase):

    def setUp(self):
        self.unidad_academica = UnidadAcademica.objects.create(
            clave_nueva='123',
            clave_antigua='312',
            nombre='Ingeniería Eléctrica'
        )

        self.programa = Programa.objects.create(
            programa='Ingeniería de Software',
            unidad_academica=self.unidad_academica
        )

        self.materia = Materia.objects.create(
            nombre = 'Introducción a la Ingeniería de Software',
            clave = '1231',
            semestre = 'Quinto Semestre',
            programa = self.programa
        )

    def test_url_nueva_materia(self):
        response = self.client.get('/docente/materias/agregar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/materia_form.html')

    def test_materia_puede_guardar_peticiones_post(self):
        self.assertEqual(Materia.objects.count(), 1)
        nueva_materia = Materia.objects.first()
        self.assertEqual(nueva_materia.nombre, self.materia.nombre)

    def test_materia_entrada_invalida_en_template_con_formulario(self):
        response = self.client.post('/docente/materias/agregar', data={'nombre': ''})
        self.assertIsInstance(response.context['form'], MateriaForm)

    def test_materia_invalidos_no_se_guardan(self):
        self.client.post('/docente/materias/agregar', data={'nombre': ''})
        # El 1 es para ver que no guardó el de la línea de arriba
        self.assertEqual(Materia.objects.count(), 1)

class CuerpoAcademicoView(TestCase):

    def test_url_lista_cuerpo_academico(self):
        response = self.client.get('/docente/cuerpos/listar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/cuerpos_list.html')

    def test_envio_datos_cuerpo_academico(self):
        response = self.client.get('/docente/cuerpos/listar')
        self.assertIn('object_list', response.context)

class CuerpoAcademicoNuevo(TestCase):

    def setUp(self):
        self.unidad_academica = UnidadAcademica.objects.create(
            clave_nueva='123',
            clave_antigua='312',
            nombre='Ingeniería Eléctrica'
        )

        self.cuerpo_academico = CuerpoAcademico.objects.create(
            no_registro='123',
            nombre ='Un nombre bien chingón',
            unidad_academica = self.unidad_academica,
            fecha_inicio = '2018-12-12',
            fecha_fin ='2019-12-12'
        )

    def test_url_nueva_cuerpo_academico(self):
        response = self.client.get('/docente/cuerpos/agregar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogos/cuerpo_form.html')

    def test_cuerpo_academico_puede_guardar_peticiones_post(self):
        self.assertEqual(CuerpoAcademico.objects.count(), 1)
        nuevo_cuerpo_academico = CuerpoAcademico.objects.first()
        self.assertEqual(nuevo_cuerpo_academico.nombre, self.cuerpo_academico.nombre)

    def test_cuerpo_academico_entrada_invalida_en_template_con_formulario(self):
        response = self.client.post('/docente/cuerpos/agregar', data={'nombre': ''})
        self.assertIsInstance(response.context['form'], CuerpoAcademicoForm)

    def test_cuerpo_academico_invalidos_no_se_guardan(self):
        self.client.post('/docente/cuerpos/agregar', data={'nombre': ''})
        # El 1 es para ver que no guardó el de la línea de arriba
        self.assertEqual(CuerpoAcademico.objects.count(), 1)