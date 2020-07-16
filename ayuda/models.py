from django.db import models
from beneficiario.models import beneficiario
from entidad.models import entidad
from datetime import datetime


# Create your models here.
class ayuda(models.Model):
    nombreAyuda = models.CharField(max_length=150, null=True)
    beneficiario = models.ForeignKey('beneficiario.Beneficiario', related_name = 'beneficiarios', null=True, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now)
    entidad = models.ForeignKey('entidad.Entidad', related_name = 'entidades', null=True, on_delete=models.CASCADE)

    def __str__(self):
            return '{}'.format(self.nombreAyuda)
