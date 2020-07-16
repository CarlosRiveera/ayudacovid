from django.db import models

# Create your models here.

class entidad(models.Model):
    nombreEntidad = models.CharField(max_length=150)
    rubro = models.CharField(max_length=150)

    def __str__(self):
            return '{}'.format(self.nombreEntidad)
