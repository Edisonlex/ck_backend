from rest_framework import serializers
from .models import ConfiguracionFAQ, PreguntaFrecuente

class ConfiguracionFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionFAQ
        fields = '__all__'

class PreguntaFrecuenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreguntaFrecuente
        fields = '__all__'