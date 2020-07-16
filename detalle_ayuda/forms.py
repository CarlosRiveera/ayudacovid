from django import forms
from .models import Detalle_ayuda

class detalleAyudaForm(forms.ModelForm):

    class Meta:
        model = Detalle_ayuda
        fields = '__all__'
        labels = {
            'ayuda': 'Seleccione ayuda',
            'tipo_ayuda': 'Seleccione el tipo de ayuda:',
            'descripcion': 'Descripcion:',
            'cantidad': 'Cantidad'
        }
        widgets = {
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
          'ayuda': forms.Select(attrs={'class': 'form-control'}),
          'tipo_ayuda': forms.Select(attrs={'class': 'form-control'})
        }

