from behave import given, when, then
from selenium import webdriver
from unittest import TestCase
import time

@given(u'que ingreso a la lista de docentes para buscar los datos de un docente')
def step_impl(context):
    context.driver.get('http://localhost:8000/docente/listar')


@when(u'escribo la curp "{curp}" en el campo de busqueda')
def step_impl(context,curp):
    caja = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div/label/input')
    caja.send_keys(curp)
    time.sleep(2)

@when(u'presiono el acciones')
def step_impl(context):
    acciones = context.driver.find_element_by_xpath('//*[@id="dropdownMenuButton"]')
    acciones.click()


@when(u'el apartado Perfil Completo')
def step_impl(context):
    perfil = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div/table/tbody/tr/td[6]/div/div/a[1]')
    perfil.click()
    time.sleep(2)


@then(u'puedo ver el perfil completo del Docente "{docente}"')
def step_impl(context,docente):
    context.test.assertIn(docente, context.driver.page_source)

@then(u'sus datos personales "{datos}"')
def step_impl(context,datos):
    context.test.assertIn(datos, context.driver.page_source)

@then(u'sus datos laboraless "{datos}"')
def step_impl(context,datos):
    context.test.assertIn(datos, context.driver.page_source)

@then(u'la tabla está vacía y me dice el mensaje "{mensaje}"')
def step_impl(context,mensaje):
    context.test.assertIn(mensaje, context.driver.page_source)

