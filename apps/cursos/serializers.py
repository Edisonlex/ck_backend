from rest_framework import serializers
from .models import (
    ConfiguracionCursos,
    Curso,
    ObjetivoCurso,
    ModuloCurso,
    TemaModulo,
    RequisitoCurso,
    BeneficioCurso
)

class TemaModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemaModulo
        fields = ['id', 'descripcion']

class ModuloCursoSerializer(serializers.ModelSerializer):
    temas = TemaModuloSerializer(many=True, read_only=True)
    
    class Meta:
        model = ModuloCurso
        fields = ['id', 'titulo', 'orden', 'temas']

class ObjetivoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetivoCurso
        fields = ['id', 'descripcion']

class RequisitoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitoCurso
        fields = ['id', 'descripcion']

class BeneficioCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficioCurso
        fields = ['id', 'descripcion']

class CursoSerializer(serializers.ModelSerializer):
    objetivos = ObjetivoCursoSerializer(many=True, read_only=True)
    modulos = ModuloCursoSerializer(many=True, read_only=True)
    requisitos = RequisitoCursoSerializer(many=True, read_only=True)
    beneficios = BeneficioCursoSerializer(many=True, read_only=True)
    modalidad_display = serializers.CharField(source='get_modalidad_display', read_only=True)
    color_display = serializers.CharField(source='get_color_display', read_only=True)
    
    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'descripcion',
            'duracion',
            'modalidad',
            'modalidad_display',
            'certificacion',
            'color',
            'color_display',
            'icono_url',
            'estudiantes',
            'nivel',
            'orden',
            'destacado',
            'objetivos',
            'modulos',
            'requisitos',
            'beneficios'
        ]

class ConfiguracionCursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionCursos
        fields = ['id', 'titulo_seccion', 'descripcion_seccion']