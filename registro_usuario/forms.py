from django import forms
from .models import usuario

class usuariosForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ('duiUsuario','nombresUsuario','apellidosUsuario','tipoUsuario')
        labels = {
            'duiUsuario': 'DUI:',
            'nombresUsuario': 'Nombres',
            'apellidosUsuario': 'Apellidos', 
            'tipoUsuario': 'Tipo de usuario'
        }

    def __init__(self, *args, **kwargs):
        super(usuariosForm,self).__init__(*args, **kwargs)   
        self.fields['tipoUsuario'].emptyLabel = "Slect"