from django import forms
from .models import entidad

class entidadForm(forms.ModelForm):
    class Meta:
        model = entidad
        fields = ('nombreEntidad','rubro')
        labels = {
            'nombreEntidad': 'Nombre:',
            'rubro': 'Rubro:',
        }
        widgets = {
          'nombreEntidad': forms.TextInput(attrs={'class': 'form-control'}),
          'rubro': forms.TextInput(attrs={'class': 'form-control'}),
        }


