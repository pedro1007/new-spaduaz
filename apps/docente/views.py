from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView

from apps.docente.forms import DatosPersonalesForm, DatosLaboralesForm, ConacytForm, ProdepForm, SniForm, \
    GradosAcademicosForm, CategoriaIncidenciasForm, CategoriaGradosForm, CuerpoAcademicoForm, \
    EscuelaForm, MateriaForm, ProgramaForm, UnidadAcademicaForm

from .models import DatosPersonales, DatosLaborales, GradosAcademicos, Conacyt, Prodep, Sni, \
    CategoriaIncidencias, CategoriaGrados, Escuela, UnidadAcademica, Programa, Materia, CuerpoAcademico


# Create your views here.

class Index(TemplateView):
    template_name = "base/base.html"


class ListaDocentes(ListView):
    model = DatosPersonales
    template_name = 'docente/lista_docente.html'


def docente_detalles(request, id):
    personales = DatosPersonales.objects.get(id=id)
    laborales = DatosLaborales.objects.get(id=id)

    grados = personales.gradosacademicos_set.all()
    conacyt = personales.conacyt_set.all()
    prodep = personales.prodep_set.all()
    sni = personales.sni_set.all()

    return render(request, 'docente/docente_detalles.html',
                  {
                      'personales': personales,
                      'laborales': laborales,
                      'grados': grados,
                      'conacyt': conacyt,
                      'prodep': prodep,
                      'sni': sni,
                  })


def docente_activate(request, id):
    docente = DatosPersonales.objects.get(id=id)
    if docente.status:
        docente.status = False
    else:
        docente.status = True

    docente.save()
    return redirect('docente:docente_listar')


class NuevoDocente(CreateView):
    model = DatosPersonales
    template_name = 'docente/docente_nuevo.html'
    form_class = DatosPersonalesForm
    laborales_form_class = DatosLaboralesForm
    conacyt_form_class = ConacytForm
    prodep_form_class = ProdepForm
    sni_form_class = SniForm

    success_url = reverse_lazy('docente:docente_listar')

    def get_context_data(self, **kwargs):
        context = super(NuevoDocente, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.laborales_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.conacyt_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.prodep_form_class(self.request.GET)
        if 'form5' not in context:
            context['form5'] = self.sni_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.laborales_form_class(request.POST)
        form3 = self.conacyt_form_class(request.POST)
        form4 = self.prodep_form_class(request.POST)
        form5 = self.sni_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            personales = form.save()
            laborales = form2.save(commit=False)
            laborales.datos_personales = personales
            laborales.save()

            conacyt = form3.save(commit=False)
            conacyt.docente = personales
            conacyt.save()
            prodep = form4.save(commit=False)
            prodep.docente = personales
            prodep.save()
            sni = form5.save(commit=False)
            sni.docente = personales
            sni.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2,form3=form3,form4=form4,form5=form5))



class ActualizaDocente(UpdateView):
    template_name = 'docente/docente_editar.html'
    model = DatosLaborales
    form_class = DatosLaboralesForm
    extra_context = {'form_personales': DatosPersonalesForm()}
    success_url = reverse_lazy('lista_clientes')

    def form_valid(self, form):
        print('valid')
        laborales = self.get_object()
        form_personales= DatosPersonalesForm(self.request.POST, self.request.FILES, instance=laborales.datos_personales)
        if not form_personales.is_valid():
            return self.render_to_response(self.get_context_data(form=form, extra_context=form_personales))
        else:
            form_personales.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        form_personales = DatosPersonalesForm(self.request.POST, self.request.FILES, instance=self.get_object().datos_personales)
        return self.render_to_response(self.get_context_data(form=form, extra_context=form_personales))

    def get_context_data(self, **kwargs):
        if 'extra_context' in kwargs:
            form_personales = kwargs['extra_context']
            self.extra_context = kwargs['extra_context'] = {'form_personales': form_personales}
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        self.extra_context = {'form_personales': DatosPersonalesForm(instance=self.get_object().datos_personales)}
        return super().get(request, *args, **kwargs)

# class NuevoDocente(CreateView):
#     model = DatosPersonales
#     form_class = DatosPersonalesForm
#     extra_context = {
#         'laborales': DatosLaboralesForm(),
#         'cona': ConacytForm(),
#         'prod': ProdepForm(),
#         'sni': SniForm(),
#     }
#     template_name = 'docente/docente_nuevo.html'
#     success_url = reverse_lazy('docente:docente_listar')
#
#     def form_invalid(self, form):
#         form_laborales = DatosLaboralesForm(self.request.POST, self.request.FILES)
#         form_conacyt = ConacytForm(self.request.POST, self.request.FILES)
#         form_prodep = ProdepForm(self.request.POST, self.request.FILES)
#         form_sni = SniForm(self.request.POST, self.request.FILES)
#         return self.render_to_response(self.get_context_data(form=form, form_laborales=form_laborales,
#                                                              form_conacyt=form_conacyt,form_prodep=form_prodep,
#                                                              form_sni=form_sni))
#
#     def get_context_data(self, **kwargs):
#         if 'extra_context' in kwargs:
#             self.extra_context = {'cliente_form': kwargs['extra_context']}
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         #form_personales = DatosPersonales(self.request.POST, self.request.FILES)
#         form_laborales = DatosLaboralesForm(self.request.POST, self.request.FILES)
#         form_conacyt = ConacytForm(self.request.POST, self.request.FILES)
#         form_prodep = ProdepForm(self.request.POST, self.request.FILES)
#         form_sni = SniForm(self.request.POST, self.request.FILES)
#         if form_laborales.is_valid() and form_conacyt.is_valid() and form_prodep.is_valid() and form_sni.is_valid():
#             personales = form.save()
#
#             laborales = form_laborales.save(commit=False)
#             laborales.datos_personales = personales
#             laborales.save()
#
#             conacyt = form_conacyt.save(commit=False)
#             conacyt.docente = personales
#             conacyt.save()
#             prodep = form_prodep.save(commit=False)
#             prodep.docente = personales
#             prodep.save()
#             sni = form_sni.save(commit=False)
#             sni.docente = personales
#             sni.save()
#
#             #return reverse_lazy('docente:docente_listar')
#
#         else:
#             return self.render_to_response(self.get_context_data(form=form, extra_context={'laborales':form_laborales,
#                                                                                            'cona':form_conacyt,
#                                                                                            'prod':form_prodep,
#                                                                                            'sni':form_sni}))
#         return super().form_valid(form)


# def docente_nuevo(request):
#     if request.method == 'POST':
#         form_personales = DatosPersonalesForm(request.POST)
#         form_laborales = DatosLaboralesForm(request.POST)
#         form_conacyt = ConacytForm(request.POST)
#         form_prodep = ProdepForm(request.POST)
#         form_sni = SniForm(request.POST)
#         if all([form_personales.is_valid(), form_laborales.is_valid(), form_conacyt.is_valid(), form_prodep.is_valid(),
#                 form_sni.is_valid()]):
#             personales = form_personales.save()
#
#             laborales = form_laborales.save(commit=False)
#             laborales.datos_personales = personales
#             laborales.save()
#
#             conacyt = form_conacyt.save(commit=False)
#             conacyt.docente = personales
#             conacyt.save()
#
#             prodep = form_prodep.save(commit=False)
#             prodep.docente = personales
#             prodep.save()
#
#             sni = form_sni.save(commit=False)
#             sni.docente = personales
#             sni.save()
#
#             return redirect('docente:docente_listar')
#         return redirect('docente:docente_listar')
#     else:
#         form_personales = DatosPersonalesForm()
#         form_laborales = DatosLaboralesForm()
#         form_conacyt = ConacytForm()
#         form_prodep = ProdepForm()
#         form_sni = SniForm()
#     return render(request, 'docente/docente_nuevo.html',
#                   {
#                       'personales': form_personales,
#                       'laborales': form_laborales,
#                       'cona': form_conacyt,
#                       'prod': form_prodep,
#                       'sni': form_sni,
#                   })


# def docente_editar(request, id):
#     docente = DatosPersonales.objects.get(pk=id)
#     laborales = DatosLaborales.objects.get(datos_personales=docente)
#     conacyt = Conacyt.objects.get(docente=docente)
#     prodep = Prodep.objects.get(docente=docente)
#     sni = Sni.objects.get(docente=docente)
#     if request.method == 'POST':
#         form_personales = DatosPersonalesForm(request.POST, instance=docente)
#         form_laborales = DatosLaboralesForm(request.POST, instance=laborales)
#         form_conacyt = ConacytForm(request.POST, instance=conacyt)
#         form_prodep = ProdepForm(request.POST, instance=prodep)
#         form_sni = SniForm(request.POST, instance=sni)
#
#         if all([form_personales.is_valid(), form_laborales.is_valid(), form_conacyt.is_valid(), form_prodep.is_valid(),
#                 form_sni.is_valid()]):
#             form_personales.save()
#             form_laborales.save()
#             form_conacyt.save()
#             form_prodep.save()
#             form_sni.save()
#
#             return redirect('docente:docente_listar')
#     else:
#         form_personales = DatosPersonalesForm(instance=docente)
#         form_laborales = DatosLaboralesForm(instance=laborales)
#         form_conacyt = ConacytForm(instance=conacyt)
#         form_prodep = ProdepForm(instance=prodep)
#         form_sni = SniForm(instance=sni)
#     return render(request, 'docente/docente_nuevo.html',
#                   {
#                       'personales': form_personales,
#                       'laborales': form_laborales,
#                       'cona': form_conacyt,
#                       'prod': form_prodep,
#                       'sni': form_sni,
#                   })


def grado_academico_nuevo(request, id):
    docente = DatosPersonales.objects.get(pk=id)
    if request.method == 'POST':
        form_grado = GradosAcademicosForm(request.POST)
        if form_grado.is_valid():
            grado = form_grado.save(commit=False)
            grado.docente = docente
            grado.save()
            return redirect('docente:docente_listar')
        return redirect('docente:docente_listar')
    else:
        form_grado = GradosAcademicosForm()
    return render(request, 'docente/grado_academico_form.html',
                  {
                      'form_grado': form_grado,
                      'docente': docente.nombres,
                  })


def grado_academico_nuevo2(request):
    return redirect('docente:docente_listar')


class CatIncidenciasList(ListView):
    model = CategoriaIncidencias
    template_name = 'catalogos/cat_incidencias_list.html'
    paginate_by = 10


class CatIncidenciaCreate(CreateView):
    model = CategoriaIncidencias
    form_class = CategoriaIncidenciasForm
    template_name = 'catalogos/cat_incidencias_form.html'
    success_url = reverse_lazy('docente:incidencias_listar')


class CatGradosList(ListView):
    model = CategoriaGrados
    template_name = 'catalogos/cat_grados_list.html'
    paginate_by = 10


class CatGradosCreate(CreateView):
    model = CategoriaGrados
    form_class = CategoriaGradosForm
    template_name = 'catalogos/cat_grados_form.html'
    success_url = reverse_lazy('docente:grados_listar')


class EscuelasList(ListView):
    model = Escuela
    template_name = 'catalogos/escuelas_list.html'
    paginate_by = 20


class EscuelaCreate(CreateView):
    model = Escuela
    form_class = EscuelaForm
    template_name = 'catalogos/escuela_form.html'
    success_url = reverse_lazy('docente:escuelas_listar')


class UnidadAcademicaList(ListView):
    model = UnidadAcademica
    template_name = 'catalogos/unidad_academica_list.html'
    paginate_by = 20


class UnidadAcademicaCreate(CreateView):
    model = UnidadAcademica
    form_class = UnidadAcademicaForm
    template_name = 'catalogos/unidad_academica_form.html'
    success_url = reverse_lazy('docente:unidades_listar')


class ProgramaList(ListView):
    model = Programa
    template_name = 'catalogos/programa_list.html'
    paginate_by = 20


class ProgramaCreate(CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'catalogos/programa_form.html'
    success_url = reverse_lazy('docente:programas_listar')


class MateriaList(ListView):
    model = Materia
    template_name = 'catalogos/materias_list.html'
    paginate_by = 20


class MateriaCreate(CreateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'catalogos/materia_form.html'
    success_url = reverse_lazy('docente:materias_listar')


class CuerpoList(ListView):
    model = CuerpoAcademico
    template_name = 'catalogos/cuerpos_list.html'
    paginate_by = 20


class CuerpoCreate(CreateView):
    model = CuerpoAcademico
    form_class = CuerpoAcademicoForm
    template_name = 'catalogos/cuerpo_form.html'
    success_url = reverse_lazy('docente:cuerpos_listar')
