
from django.urls import path
from apps.base.views import base_list,nueva_base,docente_base_list


app_name='base'
urlpatterns = [
    path('listar',base_list,name='base_listar'),
    path('bases/nuevo/<id>',nueva_base,name='base_nueva'),
    path('historial/<id>',docente_base_list, name='historial_base'),
]
