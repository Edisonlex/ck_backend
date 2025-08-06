from django.db import models

# Create your models here.
from django.db import models

class Contador(models.Model):
    años_experiencia = models.PositiveIntegerField(default=22)
    estudiantes_graduados = models.PositiveIntegerField(default=3500)
    programas_academicos = models.PositiveIntegerField(default=15)
    docentes_expertos = models.PositiveIntegerField(default=60)
    
    class Meta:
        verbose_name = "Contador"
        verbose_name_plural = "Contadores"
    
    def __str__(self):
        return "Estadísticas Principales"