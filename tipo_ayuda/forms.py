from django import forms
from .models import Tipo_ayuda

class tipoAyudaForm(forms.ModelForm):
    class Meta:
        model = Tipo_ayuda
        fields = '__all__'
        labels = {
            'nombreAyuda': 'Nombre de tipo de ayuda:',
        }
        widgets = {
          'nombreAyuda': forms.TextInput(attrs={'class': 'form-control'}),
        }