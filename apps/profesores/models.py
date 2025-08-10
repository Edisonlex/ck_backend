from django.db import models
from apps.cursos.models import Curso

COLORES_CHOICES = [
    ('bg-blue-500', 'Azul'),
    ('bg-red-500', 'Rojo'),
    ('bg-green-500', 'Verde'),
    ('bg-yellow-500', 'Amarillo'),
    ('bg-indigo-500', 'Índigo'),
    ('bg-purple-500', 'Morado'),
    ('bg-pink-500', 'Rosa'),
    ('bg-gray-500', 'Gris'),
]

class ConfiguracionProfesores(models.Model):
    titulo = models.CharField(max_length=100, default="Nuestros Profesores")
    descripcion = models.TextField(
        default="Conoce a nuestro equipo de profesionales altamente calificados que te guiarán en tu formación académica."
    )
    
    class Meta:
        verbose_name = "Configuración de Página de Profesores"
        verbose_name_plural = "Configuración de Página de Profesores"
    
    def __str__(self):
        return "Configuración de la sección de Profesores"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nombre_completo = models.CharField(max_length=200, blank=True)
    titulo = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.URLField(blank=True, null=True)
    color = models.CharField(max_length=20, choices=COLORES_CHOICES, default='bg-blue-500')
    experiencia_años = models.PositiveIntegerField(default=0)
    cursos_dictados = models.ManyToManyField(Curso, blank=True, related_name='profesores')

    def save(self, *args, **kwargs):
        self.nombre_completo = f"{self.nombre} {self.apellido}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre_completo
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ['nombre', 'apellido']