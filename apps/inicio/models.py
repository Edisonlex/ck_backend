from django.db import models

class HeroSection(models.Model):
    background_image = models.URLField(max_length=500, null=True, blank=True)
    badge_text = models.CharField(max_length=100, default="Fundación Educativa", help_text="Texto que aparece en la insignia superior")
    title = models.CharField(max_length=100, default="CKMALAU", help_text="Título principal")
    subtitle = models.CharField(max_length=200, default="Transformando vidas a través de la educación", help_text="Subtítulo debajo del título principal")
    description = models.TextField(default="Formamos profesionales competentes con valores sólidos para contribuir al desarrollo de nuestra sociedad", help_text="Descripción detallada")
    
    class Meta:
        verbose_name = "Sección Principal"
        verbose_name_plural = "Sección Principal"
    
    def __str__(self):
        return self.title