from rest_framework import generics
from .models import ConfiguracionFAQ, PreguntaFrecuente
from .serializers import ConfiguracionFAQSerializer, PreguntaFrecuenteSerializer

class ConfiguracionFAQView(generics.RetrieveAPIView):
    queryset = ConfiguracionFAQ.objects.all()
    serializer_class = ConfiguracionFAQSerializer
    
    def get_object(self):
        instance, _ = ConfiguracionFAQ.objects.get_or_create(pk=1)
        return instance

class PreguntasFrecuentesListView(generics.ListAPIView):
    queryset = PreguntaFrecuente.objects.all().order_by('orden')
    serializer_class = PreguntaFrecuenteSerializer