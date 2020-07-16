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
        widgets = {
          'duiUsuario': forms.TextInput(attrs={'class': 'form-control'}),
          'tipoUsuario': forms.Select(attrs={'class': 'form-control'}),
          'nombresUsuario': forms.TextInput(attrs={'class': 'form-control'}),
          'apellidosUsuario': forms.TextInput(attrs={'class': 'form-control'})
        }

    

