from django.db import models
from apps.ubicacion.models import Ubicacion  # Importa el modelo Ubicacion

class CallToAction(models.Model):
    titulo = models.CharField(max_length=200, default="¡Inscríbete hoy y transforma tu futuro!")
    descripcion = models.TextField(
        default="No dejes pasar la oportunidad de capacitarte con los mejores. Contáctanos por WhatsApp o visita nuestras instalaciones y da el primer paso hacia una carrera exitosa."
    )
    ubicacion = models.OneToOneField(Ubicacion, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        verbose_name = "Call To Action"
        verbose_name_plural = "Call To Action"

    def __str__(self):
        return "Configuración Call To Action"

    @property
    def whatsapp(self):
        return self.ubicacion.telefono  # accede al teléfono de Ubicacion
