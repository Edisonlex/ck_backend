from rest_framework import generics
from .models import Profesor, ConfiguracionProfesores
from .serializers import ProfesorSerializer, ConfiguracionProfesoresSerializer

class ConfiguracionProfesoresView(generics.RetrieveAPIView):
    queryset = ConfiguracionProfesores.objects.all()
    serializer_class = ConfiguracionProfesoresSerializer
    
    def get_object(self):
        instance, _ = ConfiguracionProfesores.objects.get_or_create(pk=1)
        return instance

class ProfesorListView(generics.ListAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class ProfesorDetailView(generics.RetrieveAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    lookup_field = 'id'