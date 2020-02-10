from django import forms
from django.shortcuts import redirect, render
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from apps.base import models


class BaseForm(forms.ModelForm):
    class Meta:
        model = models.Base
        fields = '__all__'
        exclude = ('datos_personales', 'oficio',)

        widgets = {
            'fecha_movimiento': DatePicker(),
        }