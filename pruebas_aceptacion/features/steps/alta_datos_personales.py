from behave import given, when, then
from selenium import webdriver
from unittest import TestCase
import time

@given(u'que ingreso al formulario para ingresar la informacion un nuevo docente')
def step_impl(context):
    context.driver.get('http://localhost:8000/docente/listar')
    boton_docente = context.driver.find_element_by_xpath('/html/body/div[1]/ul/li[2]/a')
    boton_docente.click()
    boton_nuevo = context.driver.find_element_by_xpath('/html/body/div[1]/ul/li[2]/div/div/a[2]')
    boton_nuevo.click()

@given(u'escribo los datos personales: nombres: "{nombres}", apellido paterno: "{ap_paterno}", apellido materno: "{ap_materno}"')
def step_impl(context, nombres, ap_paterno, ap_materno):
    context.driver.find_element_by_id('id_nombres').send_keys(nombres)
    context.driver.find_element_by_id('id_ap_paterno').send_keys(ap_paterno)
    context.driver.find_element_by_id('id_ap_materno').send_keys(ap_materno)


@given(u'escribo los datos personales: fecha de nacimiento: "{fecha_nacimiento}", rfc: "{rfc}", curp:"{curp}"')
def step_impl(context, fecha_nacimiento, rfc, curp):
    context.driver.find_element_by_id('id_fecha_nacimiento').send_keys(fecha_nacimiento)
    context.driver.find_element_by_id('id_rfc').send_keys(rfc)
    context.driver.find_element_by_id('id_curp').send_keys(curp)


@given(u'escribo los datos personales: nss: "{nss}", sexo: "{sexo}", estado civil:"{estado_civil}"')
def step_impl(context, nss, sexo, estado_civil):
    context.driver.find_element_by_id('id_nss').send_keys(nss)
    context.driver.find_element_by_id('id_sexo').send_keys(sexo)
    context.driver.find_element_by_id('id_estado_civil').send_keys(estado_civil)


@given(u'escribo los datos personales: domicilio: "{domicilio}", municipio: "{municipio}", estatus: "{estatus}"')
def step_impl(context, domicilio, municipio, estatus):
    context.driver.find_element_by_id('id_domicilio').send_keys(domicilio)
    context.driver.find_element_by_id('id_municipio').send_keys(municipio)
    context.driver.find_element_by_id('id_status').send_keys(estatus)


@given(u'escribo los datos laborales: matricula docente: "{matricula_docente}", matricula nomina: "{matricula_nomina}", fecha de ingreso: "{fecha_ingreso}"')
def step_impl(context, matricula_docente, matricula_nomina, fecha_ingreso):
    context.driver.find_element_by_id('id_matricula_docente').send_keys(matricula_docente)
    context.driver.find_element_by_id('id_matricula_nomina').send_keys(matricula_nomina)
    context.driver.find_element_by_id('id_fecha_ingreso').send_keys(fecha_ingreso)


@given(u'escribo los datos laborales: numero expediente: "{no_expediente}", es exclusivo: "{exclusivo}", cvu: "{cvu}", cuerpo academico:"{cuerpo_academico}", programa:"{programa}"')
def step_impl(context, no_expediente, exclusivo, cvu, cuerpo_academico, programa):
    context.driver.find_element_by_id('id_no_expediente').send_keys(no_expediente)
    context.driver.find_element_by_id('id_exclusivo').send_keys(exclusivo)
    context.driver.find_element_by_id('id_cvu').send_keys(cvu)
    context.driver.find_element_by_id('id_cuerpo_academico').send_keys(cuerpo_academico)
    opcion_programa = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/form/p[24]/select/option[1]')
    opcion_programa.click()


@given(u'escribo los datos conacyt: numero de proyecto: "{numero_proyecto}", nombre del proyecto: "{nombre_proyecto}", fecha de inicio: "{fecha_inicio}", fecha de termino: "{fecha_termino}"')
def step_impl(context, numero_proyecto, nombre_proyecto, fecha_inicio, fecha_termino):
    context.driver.find_element_by_id('id_numero_proyecto').send_keys(numero_proyecto)
    context.driver.find_element_by_id('id_nombre_proyecto').send_keys(nombre_proyecto)
    context.driver.find_element_by_id('id_fecha_inicio_conacyt').send_keys(fecha_inicio)
    context.driver.find_element_by_id('id_fecha_fin_conacyt').send_keys(fecha_termino)

@given(u'escribo los datos prodep: clave: "{clave_prodep}", descripcion: "{descripcion}", fecha de inicio: "{fecha_inicio_p}", fecha de termino: "{fecha_termino_p}", imagen prodep: "{imagen_prodep}"')
def step_impl(context, clave_prodep, descripcion, fecha_inicio_p, fecha_termino_p, imagen_prodep):
    context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/form/p[31]/input').send_keys(clave_prodep)
    context.driver.find_element_by_id('id_descripcion').send_keys(descripcion)
    context.driver.find_element_by_id('id_fecha_inicio_prodep').send_keys(fecha_inicio_p)
    context.driver.find_element_by_id('id_fecha_fin_prodep').send_keys(fecha_termino_p)
    context.driver.find_element_by_id('id_imagen_prodep').send_keys(imagen_prodep)


@given(u'escribo los datos sni: clave: "{clave_sni}", descripcion: "{descripcion}", fecha de inicio: "{fecha_inicio_s}", fecha de termino: "{fecha_termino_s}", nivel: "{nivel_sni}", imagen nivel: "{imagen_sni}"')
def step_impl(context, clave_sni, descripcion, fecha_inicio_s, fecha_termino_s, nivel_sni, imagen_sni):
    context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/form/p[38]/input').send_keys(clave_sni)
    context.driver.find_element_by_id('id_descripcion').send_keys(descripcion)
    context.driver.find_element_by_id('id_fecha_inicio_sni').send_keys(fecha_inicio_s)
    context.driver.find_element_by_id('id_fecha_fin_sni').send_keys(fecha_termino_s)
    context.driver.find_element_by_id('id_nivel').send_keys(nivel_sni)
    context.driver.find_element_by_id('id_imagen_sni').send_keys(imagen_sni)

@when(u'presiono el botón guardar de docente')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/form/button').click()

@then(u'puedo ver el docente: "{docente}" en la lista')
def step_impl(context, docente):
    time.sleep(3)
    context.test.assertIn(f'<td>{docente}</td>', context.driver.page_source)
