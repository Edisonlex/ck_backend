from rest_framework import generics
from .models import Ubicacion
from .serializers import UbicacionSerializer

class UbicacionView(generics.RetrieveAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    
    def get_object(self):
        instance, _ = Ubicacion.objects.get_or_create(pk=1)
        return instance