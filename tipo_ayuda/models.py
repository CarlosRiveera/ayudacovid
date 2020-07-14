from django.db import models

# Create your models here.

class Tipo_ayuda(models.Model):
    nombreAyuda = models.CharField(max_length=150)
