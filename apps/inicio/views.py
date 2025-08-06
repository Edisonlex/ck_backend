from rest_framework import generics
from .models import HeroSection
from .serializers import HeroSectionSerializer

class HeroSectionUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    
    def get_object(self):
        # Siempre retorna el primer (y único) registro
        return HeroSection.objects.first()
    
    def perform_create(self, serializer):
        # Sobrescribimos para evitar creación de nuevos registros
        if HeroSection.objects.exists():
            raise serializers.ValidationError("Solo puede existir un registro de HeroSection")
        serializer.save()