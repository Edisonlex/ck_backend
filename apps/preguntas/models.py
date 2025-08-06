from django.db import models

class ConfiguracionFAQ(models.Model):
    titulo_seccion = models.CharField(max_length=200, default="¿Tienes dudas?")
    descripcion_seccion = models.TextField(
        default="Aquí encontrarás respuestas a las preguntas más comunes sobre nuestros programas educativos y procesos de inscripción."
    )
    whatsapp = models.CharField(max_length=50, default="+593989985431")
    email = models.EmailField(default="info@ckmalau.edu.co")

    class Meta:
        verbose_name = "Configuración de FAQ"
        verbose_name_plural = "Configuración de FAQ"

    def __str__(self):
        return "Configuración de Preguntas Frecuentes"

class PreguntaFrecuente(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    orden = models.PositiveIntegerField(default=0, help_text="Orden de visualización")

    class Meta:
        verbose_name = "Pregunta Frecuente"
        verbose_name_plural = "Preguntas Frecuentes"
        ordering = ['orden']

    def __str__(self):
        return self.pregunta