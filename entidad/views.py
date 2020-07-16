from django.shortcuts import render, redirect
from .forms import entidadForm
from .models import entidad


# Create your views here.


def entidad_list(request):
    context = {'entidad_list': entidad.objects.all()}
    return render(request, "entidad/entidad_list.html", context)

def entidad_form(request, id=0):
    if request.method == "GET": 
        if id == 0:
            form = entidadForm()
        else:
            Entidad = entidad.objects.get(pk=id)
            form = entidadForm(instance=Entidad)
        return render(request, "entidad/entidad_form.html", {'form': form})
    else:
        if id == 0:
            form = entidadForm(request.POST)
        else:
            Entidad = entidad.objects.get(pk=id)
            form = entidadForm(request.POST,instance= Entidad)
        if form.is_valid():
            form.save()
        return redirect('/entidad/list')
    
def entidad_delete(request, id):
    Entidad = entidad.objects.get(pk=id)
    Entidad.delete()
    return redirect('/entidad/list') 