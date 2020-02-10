from behave import given, when, then
from selenium import webdriver
from unittest import TestCase
import time

@given(u'que ingreso al formulario para ingresar la informacion del grado académico del docente "{docente}"')
def step_impl(context, docente):
    context.driver.get('http://localhost:8000/docente/listar')
    table = context.driver.find_elements_by_tag_name('tbody')[0]
    rows = table.find_elements_by_tag_name('tr')
    for row in rows[0:]:
        docente_nombre = row.find_elements_by_tag_name('td')[1].text
        if docente_nombre == docente:
            acciones = row.find_element_by_class_name('btn-danger').click()
            time.sleep(1)
            boton_editar = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div/table/tbody/tr/td[6]/div/div/a[5]')
            boton_editar.click()
            break

@given(u'escribo los datos: Escuela: "{escuela}", Fecha obtencion: "{fecha_obtencion}"')
def step_impl(context, escuela, fecha_obtencion):
    context.driver.find_element_by_id('id_escuela').send_keys(escuela)
    context.driver.find_element_by_id('id_fecha_obtencion').send_keys(fecha_obtencion)
    
    
@given(u'escribo los datos: Categoria grados: "{categoria_grados}", nombre estudio: "{nombre_estudio}"')
def step_impl(context, categoria_grados, nombre_estudio):
    time.sleep(3)
    context.driver.find_element_by_id('id_categoria_grados').send_keys(categoria_grados)
    time.sleep(1)
    context.driver.find_element_by_id('id_nombre_estudio').send_keys(nombre_estudio)
    

@given(u'escribo los datos: cedula: "{cedula}" y la imagen "{imagen}"')
def step_impl(context, cedula, imagen):
    context.driver.find_element_by_id('id_cedula').send_keys(cedula)
    context.driver.find_element_by_id('id_imagen_grado').send_keys(imagen)


@when(u'presio el botón guardar')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/form/button').click()
    


@then(u'puedo ver la categoria de grado: "{cat_grado}" con el nombre de estudio: "{nom_estudio}" en la informacion escolar del docente "{docente}" en los detalles del docente')
def step_impl(context, docente, cat_grado, nom_estudio):
    #context.driver.get('http://localhost:8000/docente/listar')
    time.sleep(1)
    table = context.driver.find_elements_by_tag_name('tbody')[0]
    rows = table.find_elements_by_tag_name('tr')
    for row in rows[0:]:
        docente_nombre = row.find_elements_by_tag_name('td')[1].text
        if docente_nombre == docente:
            acciones = row.find_element_by_class_name('btn-danger').click()
            time.sleep(1)
            boton_ver = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div/table/tbody/tr/td[6]/div/div/a[1]')
            boton_ver.click()
            break

    time.sleep(1)
    context.respuesta = False
    table = context.driver.find_elements_by_tag_name('tbody')[0]
    rows = table.find_elements_by_tag_name('tr')
    for row in rows[0:]:
        cat_grado_table = row.find_elements_by_tag_name('td')[3].text
        nom_estudio_table = row.find_elements_by_tag_name('td')[4].text
        print(cat_grado_table + " " + nom_estudio_table + " VS " + cat_grado + " " + nom_estudio)
        if cat_grado_table == cat_grado and nom_estudio_table == nom_estudio:
            context.respuesta = True
            break

    res = context.respuesta
    context.test.assertTrue(res)

    # rows = context.driver.find_elements_by_tag_name('tr')
    # for row in rows[1:]:
    #     docente_nombre = row.find_elements_by_tag_name('td')[1].text
        
    #     if docente_nombre == docente:
    #         cell = row.find_elements_by_tag_name('td')[5]
    #         boton_ver_grados = cell.find_element_by_class_name('btn-info')
    #         boton_ver_grados.click()
    #         break
    # time.sleep(5)   
    # context.test.assertIn(nivel, context.driver.page_source)
    # context.test.assertIn(especialidad, context.driver.page_source)