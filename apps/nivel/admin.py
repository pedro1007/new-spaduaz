from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Bandera)
admin.site.register(models.Codificacion)
admin.site.register(models.Oficio)
admin.site.register(models.Jubilado)
admin.site.register(models.Pensionado)
admin.site.register(models.Nivel)