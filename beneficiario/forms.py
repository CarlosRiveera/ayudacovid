from django import forms
from .models import beneficiario

class beneficiarioForm(forms.ModelForm):
    class Meta:
        model = beneficiario
        fields = '__all__'
        labels = {
            'nombreBeneficiario': 'Nombre del beneficiario:',
        }
        widgets = {
          'nombreBeneficiario': forms.TextInput(attrs={'class': 'form-control'}),
        }


