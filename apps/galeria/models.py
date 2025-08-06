from django.db import models

class ConfiguracionGaleria(models.Model):
    titulo_seccion = models.CharField(max_length=200, default="Nuestros Estudiantes en Acción")
    descripcion_seccion = models.TextField(
        default="Descubre el ambiente de aprendizaje dinámico y las experiencias prácticas que viven nuestros estudiantes día a día."
    )

    class Meta:
        verbose_name = "Configuración de Galería"
        verbose_name_plural = "Configuración de Galería"

    def __str__(self):
        return "Configuración de la Galería"

class GaleriaImagen(models.Model):
    imagen_url = models.URLField(max_length=500, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0, help_text="Orden de visualización")
    destacada = models.BooleanField(default=False, help_text="Mostrar en carrusel principal")

    class Meta:
        verbose_name = "Imagen de Galería"
        verbose_name_plural = "Galería de Imágenes"
        ordering = ['orden']

    def __str__(self):
        return self.titulo