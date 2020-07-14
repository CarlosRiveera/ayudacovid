from django.shortcuts import render, redirect
from .forms import usuariosForm
from .models import usuario


# Create your views here.


def user_list(request):
    context = {'user_list': usuario.objects.all()}
    return render(request, "registro_usuario/user_list.html", context)

def user_form(request, id=0):
    if request.method == "GET": 
        if id == 0:
            form = usuariosForm()
        else:
            Usuario = usuario.objects.get(pk=id)
            form = usuariosForm(instance=Usuario)
        return render(request, "registro_usuario/user_form.html", {'form': form})
    else:
        if id == 0:
            form = usuariosForm(request.POST)
        else:
            Usuario = usuario.objects.get(pk=id)
            form = usuariosForm(request.POST,instance= Usuario)
        if form.is_valid():
            form.save()
        return redirect('/usuario/list')
    
def user_delete(request, id):
    Usuario = usuario.objects.get(pk=id)
    Usuario.delete()
    return redirect('/usuario/list') 