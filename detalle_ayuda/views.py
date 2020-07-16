from django.shortcuts import render, redirect
from .forms import detalleAyudaForm
from .models import Detalle_ayuda


# Create your views here.


def detalle_ayuda_list(request):
    context = {'detalle_ayuda_list': Detalle_ayuda.objects.all()}
    return render(request, "detalle_ayuda/detalle_ayuda_list.html", context)

def detalle_ayuda_form(request, id=0):
    if request.method == "GET": 
        if id == 0:
            form = detalleAyudaForm()
        else:
            detalle_ayuda = Detalle_ayuda.objects.get(pk=id)
            form = detalleAyudaForm(instance=detalle_ayuda)
        return render(request, "detalle_ayuda/detalle_ayuda_form.html", {'form': form})
    else:
        if id == 0:
            form = detalleAyudaForm(request.POST)
        else:
            detalle_ayuda = Detalle_ayuda.objects.get(pk=id)
            form = detalleAyudaForm(request.POST,instance= detalle_ayuda)
        if form.is_valid():
            form.save()
        return redirect('/detalleAyuda/list')
    
def detalle_ayuda_delete(request, id):
    detalle_ayuda = Detalle_ayuda.objects.get(pk=id)
    detalle_ayuda.delete()
    return redirect('/detalleAyuda/list') 