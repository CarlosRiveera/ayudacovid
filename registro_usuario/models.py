from django.db import models

# Create your models here.


class Tipo_usuario(models.Model):
    nombreTipo = models.CharField(max_length=150)
    def __str__(self):
        return self.nombreTipo  

class usuario(models.Model):
    nombresUsuario = models.CharField(max_length=150)
    apellidosUsuario = models.CharField(max_length=150)
    duiUsuario = models.CharField(max_length=150)
    tipoUsuario = models.ForeignKey(Tipo_usuario, on_delete = models.CASCADE)
    