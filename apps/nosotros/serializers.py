from rest_framework import serializers
from .models import InformacionInstitucional

class InformacionInstitucionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacionInstitucional
        fields = '__all__'