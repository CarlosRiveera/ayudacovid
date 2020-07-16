from django.db import models

# Create your models here.

class beneficiario(models.Model):
    nombreBeneficiario = models.CharField(max_length=140)
    
    def __str__(self):
        return '{}'.format(self.nombreBeneficiario)

