from django.shortcuts import render, redirect
from .forms import tipoAyudaForm
from .models import Tipo_ayuda

# Create your views here.

def tipo_ayuda_list(request):
    context = {'tipo_ayuda_list': Tipo_ayuda.objects.all()}
    return render(request, "tipo_ayuda/tipo_ayuda_list.html", context)

def tipo_ayuda_form(request, id=0):
    if request.method == "GET": 
        if id == 0:
            form = tipoAyudaForm()
        else:
            tipo_ayuda = Tipo_ayuda.objects.get(pk=id)
            form = tipoAyudaForm(instance=tipo_ayuda)
        return render(request, "tipo_ayuda/tipo_ayuda_form.html", {'form': form})
    else:
        if id == 0:
            form = tipoAyudaForm(request.POST)
        else:
            tipo_ayuda = Tipo_ayuda.objects.get(pk=id)
            form = tipoAyudaForm(request.POST,instance= tipo_ayuda)
        if form.is_valid():
            form.save()
        return redirect('/tipoAyuda/list')

def tipo_ayuda_delete(request, id):
    tipo_ayuda = Tipo_ayuda.objects.get(pk=id)
    tipo_ayuda.delete()
    return redirect('/tipoAyuda/list') 

