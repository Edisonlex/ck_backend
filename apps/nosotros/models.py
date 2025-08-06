from django.db import models

class InformacionInstitucional(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Más de 22 años formando profesionales con excelencia")
    descripcion_principal = models.TextField(default="Somos una institución educativa comprometida con la formación integral de profesionales competentes...")
    mision_titulo = models.CharField(max_length=100, default="Nuestra Misión")
    mision_descripcion = models.TextField(default="Formar profesionales íntegros y competentes...")
    vision_titulo = models.CharField(max_length=100, default="Nuestra Visión")
    vision_descripcion = models.TextField(default="Ser reconocidos como la institución educativa líder...")
    años_experiencia = models.PositiveIntegerField(default=22)

    class Meta:
        verbose_name = "Información Institucional"
        verbose_name_plural = "Información Institucional"

    def __str__(self):
        return "Información Institucional"