from django import forms
from django.shortcuts import redirect, render
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

from apps.docente import models
from apps.docente.models import LONGITUD_MAXIMA, DatosPersonales

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.DatosPersonales
        labels={
            'nombres':'Nombre(s)',
            'ap_paterno':'Apellido paterno',
            'ap_materno':'Apellido materno',
            'fecha_nacimiento':'Fecha nacimiento',
            'rfc':'RFC',
            'curp':'CURP',
            'nss':'NSS',
            'sexo':'Sexo',
            'estado_civil':'Estado civil',
            'domicilio':'Domicilio',
            'municipio':'Municipio',
            'status':'Status',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'ap_materno': forms.TextInput(attrs={'class':'form-control'}),
            'ap_paterno': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': DatePicker(),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'nss': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': DatePicker(),
        }

        error_messages = {
            'nombre': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'},
            'rfc': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'},
            'curp': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'},
            'ap_paterno': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'},
            'ap_materno': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'},
            'nss': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'},
            'domicilio': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }


class DatosLaboralesForm(forms.ModelForm):
    class Meta:
        model = models.DatosLaborales
        fields = '__all__'
        exclude = ('datos_personales',)
        labels={
            'matricula_docente':'Matricula de docente',
            'matricula_nomina':'Matricula de nomina',
            'fecha_ingreso':'Fecha de ingreso',
            'no_expediente':'Número de expediente',
            'exclusivo':'¿Es exclusivo?',
            'observaciones_exc':'Observaciones',
            'cvu':'CVU',
            'cuerpo_academico':'Cuerpo academico',
            'observaciones_c_a':'Observaciones',
            'programa':'Programa'
        }
        widgets = {
            'matricula_docente':forms.TextInput(attrs={'class':'form-control'}),
            'matricula_nomina':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ingreso':DatePicker(),
            'no_expediente':forms.TextInput(attrs={'class':'form-control'}),
            'cvu':forms.TextInput(attrs={'class':'form-control'}),
            'observaciones_c_a':forms.TextInput(attrs={'class':'form-control'})
        }


class ConacytForm(forms.ModelForm):
    class Meta:
        model = models.Conacyt
        fields = '__all__'
        exclude = ('docente',)
        widgets={
            'numero_proyecto':forms.TextInput(attrs={'class':'form-control'}),
            'nombre_proyecto':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio_conacyt':DatePicker(),
            'fecha_fin_conacyt':DatePicker(),
        }
        labels={
            'numero_proyecto':'Numero del proyecto',
            'nombre_proyecto':'Nombre del proyecto',
            'fecha_inicio_conacyt':'Fecha de inicio',
            'fecha_fin_conacyt':'Fecha de termino'
        }

        error_messages = {
            'numero_proyecto': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'},
            'nombre_proyecto': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }


class ProdepForm(forms.ModelForm):

    class Meta:
        model = models.Prodep
        fields = '__all__'
        exclude = ('docente',)
        widgets = {
            'clave':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio_prodep': DatePicker(),
            'fecha_fin_prodep': DatePicker(),
        }
        labels={
            'clave':'Clave',
            'descripcion':'Descripcion',
            'fecha_inicio_prodep':'Fecha de inicio',
            'fecha_fin_prodep':'Fecha de termino',
            'imagen_prodep':'Documento'
        }
        error_messages = {
            'clave': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }

class SniForm(forms.ModelForm):

    class Meta:
        model = models.Sni
        fields = '__all__'
        exclude = ('docente',)
        widgets = {
            'clave':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio_sni': DatePicker(),
            'fecha_fin_sni': DatePicker(),
        }
        labels={
            'clave':'Clave',
            'descripcion':'Descripcion',
            'fecha_inicio_sni':'Fecha de inicio',
            'fecha_fin_sni':'Fecha de termino',
            'nivel':'Nivel',
            'imagen_sni':'Imagen'
        }
        error_messages = {
            'clave': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }

class GradosAcademicosForm(forms.ModelForm):
    fecha_obtencion = forms.DateField(widget=DatePicker())

    class Meta:
        model = models.GradosAcademicos
        fields = '__all__'
        exclude = ('docente',)

        error_messages = {
            'nombre_estudio': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'},
            'cedula': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }


class CategoriaIncidenciasForm(forms.ModelForm):

    class Meta:
        model = models.CategoriaIncidencias
        fields = '__all__'

        error_messages = {
            'permiso': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }

class CategoriaGradosForm(forms.ModelForm):

    class Meta:
        model = models.CategoriaGrados
        fields = '__all__'

        error_messages = {
            'desc': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }

class EscuelaForm(forms.ModelForm):

    class Meta:
        model = models.Escuela
        fields = '__all__'

        error_messages = {
            'nombre': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }

class UnidadAcademicaForm(forms.ModelForm):

    class Meta:
        model = models.UnidadAcademica
        fields = '__all__'

        error_messages = {
            'nombre': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }

class ProgramaForm(forms.ModelForm):

    class Meta:
        model = models.Programa
        fields = '__all__'

        error_messages = {
            'programa': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }

class MateriaForm(forms.ModelForm):

    class Meta:
        model = models.Materia
        fields = '__all__'

        error_messages = {
            'nombre': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }

class CuerpoAcademicoForm(forms.ModelForm):

    class Meta:
        model = models.CuerpoAcademico
        fields = '__all__'

        error_messages = {
            'nombre': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'},
            'no_registro': {'max_length': LONGITUD_MAXIMA, 'required': 'Se requiere'}
        }