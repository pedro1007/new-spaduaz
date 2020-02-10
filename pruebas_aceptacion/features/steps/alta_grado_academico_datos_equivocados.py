from behave import given, when, then
from selenium import webdriver
from unittest import TestCase
import time


@given(u'escribo los datos: Categoria de grados: "{categoria_grado}"')
def step_impl(context, categoria_grado):
    time.sleep(3)
    context.driver.find_element_by_id('id_categoria_grados').send_keys(categoria_grado)


@then(u'permanezco en el mismo formulario ya que me falto ingresar la institucion')
def step_impl(context):
    context.test.assertIn('<h6 class="m-0 font-weight-bold text-primary">Nuevo grado academico para el docente José Andres</h6>', context.driver.page_source)