from django import forms
from .models import ayuda, beneficiario

class ayudaForm(forms.ModelForm):

    class Meta:
        model = ayuda
        fields = '__all__'
        labels = {
            'nombreAyuda': 'Nombre de la ayuda',
            'beneficiarios': 'Beneficiario:',
            'entidad': 'Enridad:',
            'fecha': 'Fecha'
        }
        widgets = {
          'nombreAyuda': forms.TextInput(attrs={'class': 'form-control'}),
          'beneficiario': forms.Select(attrs={'class': 'form-control'}),
          'entidad': forms.Select(attrs={'class': 'form-control'})
        }

