from rest_framework import generics
from .models import Contador
from .serializers import ContadorSerializer

class ContadorAPIView(generics.RetrieveAPIView):
    queryset = Contador.objects.all()
    serializer_class = ContadorSerializer
    
    def get_object(self):
        # Siempre devuelve el primer registro (o crea uno si no existe)
        instance, _ = Contador.objects.get_or_create(pk=1)
        return instance