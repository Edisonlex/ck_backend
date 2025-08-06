from rest_framework import serializers
from .models import CallToAction

class CallToActionSerializer(serializers.ModelSerializer):
    telefono = serializers.CharField(source='ubicacion.telefono', read_only=True)

    class Meta:
        model = CallToAction
        fields = ['id', 'titulo', 'descripcion', 'telefono']  # Ya no incluyes 'ubicacion' si no lo necesitas