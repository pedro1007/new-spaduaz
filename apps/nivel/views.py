from django.db.models import Max
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from apps.docente.models import DatosPersonales
from apps.nivel.models import Nivel, Bandera, Codificacion, Oficio
from apps.nivel.forms import BanderaForm,CodificacionForm,OficioForm,NivelForm

# Create your views here.
class ListaBase(ListView):
    model = Bandera
    # permission_required = 'dinosaurios.view_dinosaurio'
    
def nivel_list(request):
    # docente = DatosPersonales.objects.all()
    # niveles = Nivel.objects.all()
    #
    # docente_niveles = docente.


    ## Por ahora solo muestra los que ya tienen un nivel, hay que ver como hacer un
    # outer join para mostrar tambien los que no tiene nivel

    ultimos_niveles_ids = DatosPersonales.objects.annotate(
        ultimo_nivel_id=Max('nivel__id')).values_list('ultimo_nivel_id', flat=True)
    ultimos_niveles = Nivel.objects.filter(id__in=ultimos_niveles_ids).order_by('datos_personales__nombres')

    #lista = zip(docentes, niveles)
    context = {
        'niveles': ultimos_niveles,
    }
    return render(request, 'nivel/lista_niveles.html', context)



class BanderaList(ListView):
    model = Bandera
    template_name = 'catalogos/banderas_list.html'
    paginate_by = 10


class BanderaCreate(CreateView):
    model = Bandera
    form_class = BanderaForm
    template_name = 'catalogos/bandera_form.html'
    success_url = reverse_lazy('nivel:banderas_listar')


class CodificacionList(ListView):
    model = Codificacion
    template_name = 'catalogos/codificaciones_list.html'
    paginate_by = 10


class CodificacionCreate(CreateView):
    model = Codificacion
    form_class = CodificacionForm
    template_name = 'catalogos/codificaciones_form.html'
    success_url = reverse_lazy('nivel:codificiaciones_listar')
    
    
def nuevo_nivel(request, id):
    docente = DatosPersonales.objects.get(pk=id)
    if request.method == 'POST':
        form_nivel = NivelForm(request.POST)
        form_oficio = OficioForm(request.POST)
        if form_nivel.is_valid() and form_oficio.is_valid():
            nivel = form_nivel.save(commit=False)
            oficio = form_oficio.save()
            
            nivel.datos_personales = docente
            nivel.oficio = oficio
            
            nivel.save()
            return redirect('nivel:nivel_listar')
        return redirect('nivel:nivel_listar')
    else:
        form_nivel = NivelForm()
        form_oficio = OficioForm()
    return render(request, 'nivel/nivel_form.html',
                  {
                      'form_nivel': form_nivel,
                      'form_oficio':form_oficio,
                      'docente': docente.nombres,
                  })

def docente_nivel_list(request,id):
    docente = DatosPersonales.objects.get(pk=id)
    niveles = docente.nivel_set.all().order_by('fecha_movimiento')

    #lista = zip(docentes, niveles)
    context = {
        'docente':docente,
        'niveles': niveles,
    }
    return render(request, 'nivel/lista_niveles_docente.html', context)