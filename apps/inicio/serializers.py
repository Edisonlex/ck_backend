from rest_framework import serializers
from .models import HeroSection

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'
        read_only_fields = ('id',)  # Hacer el ID de solo lectura