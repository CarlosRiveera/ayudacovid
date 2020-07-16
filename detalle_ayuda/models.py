from django.db import models
from ayuda.models import ayuda
from tipo_ayuda.models import Tipo_ayuda


# Create your models here.
class Detalle_ayuda(models.Model):
    ayuda = models.ForeignKey('ayuda.Ayuda', related_name = 'ayuda', null=True, on_delete=models.CASCADE)
    tipo_ayuda = models.ForeignKey('tipo_ayuda.Tipo_ayuda', related_name = 'tipo_ayuda', null=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    cantidad = models.FloatField(max_length=150)
    
    def __str__(self):
            return '{}'.format(self.ayuda)

