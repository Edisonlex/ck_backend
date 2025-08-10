from rest_framework import serializers
from .models import Profesor, ConfiguracionProfesores

class ProfesorSerializer(serializers.ModelSerializer):
    cursos_dictados = serializers.SerializerMethodField()
    
    class Meta:
        model = Profesor
        fields = [
            'id',
            'nombre',
            'apellido',
            'nombre_completo',
            'titulo',
            'especialidad',
            'descripcion',
            'foto',
            'color',
            'experiencia_años',
            'cursos_dictados'
        ]
        read_only_fields = ['nombre_completo']
    
    def get_cursos_dictados(self, obj):
        # Retorna solo una lista con los títulos de los cursos
        return [curso.titulo for curso in obj.cursos_dictados.all()]

class ConfiguracionProfesoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionProfesores
        fields = ['id', 'titulo', 'descripcion']