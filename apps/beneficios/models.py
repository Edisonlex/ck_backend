from django.db import models

class Beneficios(models.Model):
    titulo_seccion = models.CharField(max_length=200, default="UNA EDUCACIÓN ENFOCADA EN TU ÉXITO")
    subtitulo_seccion = models.TextField(default="Te brindamos las herramientas y el apoyo que necesitas para alcanzar tus metas profesionales.")
    beneficio1_titulo = models.CharField(max_length=100, default="Docentes Capacitados")
    beneficio1_descripcion = models.TextField(default="Personal docente altamente calificado.")
    beneficio2_titulo = models.CharField(max_length=100, default="Materiales Gratuitos")
    beneficio2_descripcion = models.TextField(default="Incluimos todos los materiales sin costo adicional.")
    beneficio3_titulo = models.CharField(max_length=100, default="Formación Práctica")
    beneficio3_descripcion = models.TextField(default="Programas actualizados y orientados al desarrollo profesional.")
    beneficio4_titulo = models.CharField(max_length=100, default="Rápida Inserción Laboral")
    beneficio4_descripcion = models.TextField(default="Te preparamos para integrarte de forma inmediata al campo laboral.")

    class Meta:
        verbose_name = "Beneficios"
        verbose_name_plural = "Beneficios"

    def __str__(self):
        return "Beneficios de la Institución"