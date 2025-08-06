from rest_framework import serializers
from .models import ConfiguracionGaleria, GaleriaImagen

class ConfiguracionGaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionGaleria
        fields = '__all__'


class GaleriaImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = GaleriaImagen
        fields = ['id', 'imagen_url', 'titulo', 'descripcion', 'orden', 'destacada']
        # imagen_url ahora es un campo directo del modelo, no necesita SerializerMethodField