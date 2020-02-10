from behave import given, when, then
from selenium import webdriver
from unittest import TestCase
import time


@given(u'escribo los datos personales: apellido paterno: "{ap_paterno}", apellido materno: "{ap_materno}"')
def step_impl(context, ap_paterno,ap_materno):
    context.driver.find_element_by_id('id_ap_paterno').send_keys(ap_paterno)
    context.driver.find_element_by_id('id_ap_materno').send_keys(ap_materno)

@then(u'permanezco en el mismo formulario ya que me falto ingresar datos')
def step_impl(context):
    nuevo_docente = context.driver.find_element_by_tag_name('h6')
    context.test.assertIn('<h6 class="m-0 font-weight-bold text-primary">Nuevo Docente</h6>', context.driver.page_source)
    
