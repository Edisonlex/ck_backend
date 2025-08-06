from rest_framework import serializers
from .models import WhatsAppConfig

class WhatsAppConfigSerializer(serializers.ModelSerializer):
    telefono = serializers.CharField(source='ubicacion.telefono', read_only=True)

    class Meta:
        model = WhatsAppConfig
        fields = ['telefono', 'mensaje_predeterminado']
