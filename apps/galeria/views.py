from rest_framework import generics
from .models import ConfiguracionGaleria, GaleriaImagen
from .serializers import ConfiguracionGaleriaSerializer, GaleriaImagenSerializer

class GaleriaConfigView(generics.RetrieveAPIView):
    queryset = ConfiguracionGaleria.objects.all()
    serializer_class = ConfiguracionGaleriaSerializer
    
    def get_object(self):
        instance, _ = ConfiguracionGaleria.objects.get_or_create(pk=1)
        return instance

class GaleriaListView(generics.ListAPIView):
    queryset = GaleriaImagen.objects.filter(destacada=True).order_by('orden')
    serializer_class = GaleriaImagenSerializer