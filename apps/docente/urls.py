"""SAPDUAZ2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from apps.docente import views

app_name = 'docente'
urlpatterns = [
    path('listar', views.ListaDocentes.as_view(), name='docente_listar'),
    path('activar/<id>', views.docente_activate, name='docente_activar'),
    path('nuevo/', views.NuevoDocente.as_view(), name='docente_nuevo'),
    path('gradonuevo/<id>', views.grado_academico_nuevo, name='grado_nuevo'),
    path('gradonuevo/', views.grado_academico_nuevo2, name='grado_nuevo2'),
    path('editar/<pk>', views.ActualizaDocente.as_view(), name='docente_editar'),
    path('detalles/<id>', views.docente_detalles, name='docente_detalles'),

    path('grados/listar', views.CatGradosList.as_view(), name='grados_listar'),
    path('incidencias/listar', views.CatIncidenciasList.as_view(), name='incidencias_listar'),
    path('cuerpos/listar', views.CuerpoList.as_view(), name='cuerpos_listar'),
    path('escuelas/listar', views.EscuelasList.as_view(), name='escuelas_listar'),
    path('materias/listar', views.MateriaList.as_view(), name='materias_listar'),
    path('programas/listar', views.ProgramaList.as_view(), name='programas_listar'),
    path('unidades/listar', views.UnidadAcademicaList.as_view(), name='unidades_listar'),

    path('grados/agregar', views.CatGradosCreate.as_view(), name='grados_agregar'),
    path('incidencias/agregar', views.CatIncidenciaCreate.as_view(), name='incidencias_agregar'),
    path('cuerpos/agregar', views.CuerpoCreate.as_view(), name='cuerpos_agregar'),
    path('escuelas/agregar', views.EscuelaCreate.as_view(), name='escuelas_agregar'),
    path('materias/agregar', views.MateriaCreate.as_view(), name='materias_agregar'),
    path('programas/agregar', views.ProgramaCreate.as_view(), name='programas_agregar'),
    path('unidades/agregar', views.UnidadAcademicaCreate.as_view(), name='unidades_agregar'),

]
