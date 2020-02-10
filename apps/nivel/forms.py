from django import forms
from django.shortcuts import redirect, render
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

from apps.nivel import models
from apps.nivel.models import LONGITUD_MAXIMA


class BanderaForm(forms.ModelForm):
    class Meta:
        model = models.Bandera
        fields = '__all__'

        error_messages = {
            'nombre': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }


class CodificacionForm(forms.ModelForm):
    class Meta:
        model = models.Codificacion
        fields = '__all__'

class OficioForm(forms.ModelForm):
    class Meta:
        model = models.Oficio
        fields = '__all__'
        widgets={
            'fecha_oficio':DatePicker(),
        }
        
class NivelForm(forms.ModelForm):
    class Meta:
        model = models.Nivel
        fields = '__all__'
        exclude = ('datos_personales','oficio',)
        
        widgets={
            'fecha_movimiento':DatePicker(),
        }