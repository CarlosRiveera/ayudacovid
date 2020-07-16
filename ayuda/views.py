from django.shortcuts import render, redirect
from .forms import ayudaForm
from .models import ayuda


# Create your views here.


def ayuda_list(request):
    context = {'ayuda_list': ayuda.objects.all()}
    return render(request, "ayuda/ayuda_list.html", context)

def ayuda_form(request, id=0):
    if request.method == "GET": 
        if id == 0:
            form = ayudaForm()
        else:
            Ayuda = ayuda.objects.get(pk=id)
            form = ayudaForm(instance=Ayuda)
        return render(request, "ayuda/ayuda_form.html", {'form': form})
    else:
        if id == 0:
            form = ayudaForm(request.POST)
        else:
            Ayuda = ayuda.objects.get(pk=id)
            form = ayudaForm(request.POST,instance= Ayuda)
        if form.is_valid():
            form.save()
        return redirect('/ayuda/list')
    
def ayuda_delete(request, id):
    Ayuda = ayuda.objects.get(pk=id)
    Ayuda.delete()
    return redirect('/ayuda/list') 