from django.db import models

MODALIDAD_CHOICES = [
    ('PRESENCIAL', 'Presencial'),
    ('VIRTUAL', 'Virtual'),
    ('HIBRIDA', 'Híbrida'),
]

COLOR_CHOICES = [
    ('bg-blue-500', 'Azul'),
    ('bg-red-500', 'Rojo'),
    ('bg-green-500', 'Verde'),
    ('bg-yellow-500', 'Amarillo'),
    ('bg-indigo-500', 'Indigo'),
    ('bg-purple-500', 'Morado'),
    ('bg-pink-500', 'Rosa'),
    ('bg-gray-500', 'Gris'),
]

class ConfiguracionCursos(models.Model):
    titulo_seccion = models.CharField(max_length=200, default="Programas de Formación")
    descripcion_seccion = models.TextField(
        default="Descubre nuestros programas educativos diseñados para brindarte las habilidades y conocimientos necesarios para destacar en tu campo profesional."
    )

    class Meta:
        verbose_name = "Configuración de Cursos"
        verbose_name_plural = "Configuración de Cursos"

    def __str__(self):
        return "Configuración de la sección de Cursos"

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=20, choices=MODALIDAD_CHOICES, default='PRESENCIAL')
    certificacion = models.CharField(max_length=100)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default="bg-blue-500")
    icono_url = models.URLField(blank=True, null=True)
    estudiantes = models.PositiveIntegerField(default=0)
    nivel = models.CharField(max_length=50)
    orden = models.PositiveIntegerField(default=0)
    destacado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['orden']

    def __str__(self):
        return self.titulo

class ObjetivoCurso(models.Model):
    curso = models.ForeignKey(Curso, related_name='objetivos', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Objetivo del Curso"
        verbose_name_plural = "Objetivos del Curso"

class ModuloCurso(models.Model):
    curso = models.ForeignKey(Curso, related_name='modulos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Módulo del Curso"
        verbose_name_plural = "Módulos del Curso"
        ordering = ['orden']

class TemaModulo(models.Model):
    modulo = models.ForeignKey(ModuloCurso, related_name='temas', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Tema del Módulo"
        verbose_name_plural = "Temas del Módulo"

class RequisitoCurso(models.Model):
    curso = models.ForeignKey(Curso, related_name='requisitos', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Requisito del Curso"
        verbose_name_plural = "Requisitos del Curso"

class BeneficioCurso(models.Model):
    curso = models.ForeignKey(Curso, related_name='beneficios', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Beneficio del Curso"
        verbose_name_plural = "Beneficios del Curso"