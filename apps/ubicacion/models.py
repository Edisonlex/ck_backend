from django.db import models

class Ubicacion(models.Model):
    titulo_seccion = models.CharField(max_length=200, default="Visítanos")
    descripcion_seccion = models.TextField(
        default="Estamos ubicados en el corazón de La Maná, Ecuador. Ven y conoce nuestras instalaciones modernas y equipadas para tu formación profesional."
    )
    direccion = models.TextField(default="Av. 19 de Mayo y Calabí\nLa Maná, Cotopaxi, Ecuador")
    horarios = models.TextField(default="Lunes a Viernes: 09:00 - 17:00\nSábados y Domingos: 08:00 - 17:00")
    telefono = models.CharField(max_length=50, default="+593 98 998 5431")
    email = models.EmailField(default="info@ckmalau.edu.co")
    como_llegar = models.TextField(
        default="Ubicados en la intersección de la Av. 19 de Mayo y Calabí, cerca del centro de La Maná.\nFácil acceso en transporte público y privado."
    )
    mapa_embed = models.TextField(
        default="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d498.65954980920674!2d-79.3255736740935!3d-0.9443529139530739!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1ses-419!2sec!4v1754021089120!5m2!1ses-419!2sec"
    )

    class Meta:
        verbose_name = "Configuración de Ubicación"
        verbose_name_plural = "Configuración de Ubicación"

    def __str__(self):
        return self.telefono