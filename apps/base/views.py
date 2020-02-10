from django.shortcuts import render, redirect
from django.db.models import Max
from apps.docente.models import DatosPersonales
from apps.base.models import Base
from apps.base.forms import  BaseForm
from apps.nivel.forms import OficioForm

# Create your views here.

def base_list(request):

    ## Por ahora solo muestra los que ya tienen un nivel, hay que ver como hacer un
    # outer join para mostrar tambien los que no tiene nivel

    ultimas_bases_ids = DatosPersonales.objects.annotate(
        ultima_base_id=Max('base__id')).values_list('ultima_base_id', flat=True)
    #
    ultimas_bases = Base.objects.filter(id__in=ultimas_bases_ids).order_by('datos_personales__nombres')

    #lista = zip(docentes, niveles)
    context = {
        'bases': ultimas_bases,
    }
    return render(request, 'base_docente/lista_bases.html', context)


def nueva_base(request, id):
    docente = DatosPersonales.objects.get(pk=id)
    if request.method == 'POST':
        form_base = BaseForm(request.POST)
        form_oficio = OficioForm(request.POST)
        if form_base.is_valid() and form_oficio.is_valid():
            base = form_base.save(commit=False)
            oficio = form_oficio.save()

            base.datos_personales = docente
            base.oficio = oficio

            base.save()
            return redirect('base:base_listar')
        return redirect('base:base_listar')
    else:
        form_base = BaseForm()
        form_oficio = OficioForm()
    return render(request, 'base_docente/base_form.html',
                  {
                      'form_base': form_base,
                      'form_oficio': form_oficio,
                      'docente': docente.nombres,
                  })


def docente_base_list(request, id):
    docente = DatosPersonales.objects.get(pk=id)
    bases = docente.base_set.all().order_by('fecha_movimiento')

    # lista = zip(docentes, niveles)
    context = {
        'docente': docente,
        'bases': bases,
    }
    return render(request, 'base_docente/lista_bases_docente.html', context)