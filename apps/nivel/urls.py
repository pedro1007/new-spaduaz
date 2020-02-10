from django.urls import path
from apps.nivel.views import nivel_list, BanderaList, BanderaCreate, CodificacionCreate, CodificacionList,nuevo_nivel,\
    docente_nivel_list


app_name='nivel'
urlpatterns = [
    path('listar',nivel_list,name='nivel_listar'),

    path('bandera/lista', BanderaList.as_view(),name='bandera_listar'),
    path('bandera/nueva',BanderaCreate.as_view(),name='bandera_agregar'),
    path('codificacion/lista', CodificacionList.as_view(), name='codificacion_listar'),
    path('codificacion/nueva', CodificacionCreate.as_view(), name='codificacion_agregar'),
    
    path('niveles/nuevo/<id>',nuevo_nivel,name='nivel_nuevo'),
    path('historial/<id>',docente_nivel_list, name='historial_nivel')
]
