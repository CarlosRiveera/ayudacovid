from django.shortcuts import render, redirect
from .forms import beneficiarioForm
from .models import beneficiario


# Create your views here.


def beneficiario_list(request):
    context = {'beneficiario_list': beneficiario.objects.all()}
    return render(request, "beneficiario/beneficiario_list.html", context)

def beneficiario_form(request, id=0):
    if request.method == "GET": 
        if id == 0:
            form = beneficiarioForm()
        else:
            Beneficiario = beneficiario.objects.get(pk=id)
            form = beneficiarioForm(instance=Beneficiario)
        return render(request, "beneficiario/beneficiario_forms.html", {'form': form})
    else:
        if id == 0:
            form = beneficiarioForm(request.POST)
        else:
            Beneficiario = beneficiario.objects.get(pk=id)
            form = beneficiarioForm(request.POST,instance= Beneficiario)
        if form.is_valid():
            form.save()
        return redirect('/beneficiario/list')
    
def beneficiario_delete(request, id):
    Beneficiario = beneficiario.objects.get(pk=id)
    Beneficiario.delete()
    return redirect('/beneficiario/list') 