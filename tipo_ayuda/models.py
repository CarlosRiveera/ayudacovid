from django.db import models

class Tipo_ayuda(models.Model):
    nombreAyuda = models.CharField(max_length=150)

    def __str__(self):
            return '{}'.format(self.nombreAyuda)
