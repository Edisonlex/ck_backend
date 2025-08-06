from django.db import models
from apps.ubicacion.models import Ubicacion 

class WhatsAppConfig(models.Model):
    ubicacion = models.OneToOneField(Ubicacion, on_delete=models.CASCADE, null=True, blank=True)
    mensaje_predeterminado = models.TextField(
        default="Hola, me interesa obtener información sobre los cursos de CKMALAU"
    )

    class Meta:
        verbose_name = "Configuración WhatsApp"
        verbose_name_plural = "Configuración WhatsApp"

    def __str__(self):
        return "Configuración WhatsApp"
    
    @property
    def whatsapp(self):
        return self.ubicacion.telefono  # accede al teléfono de Ubicacion