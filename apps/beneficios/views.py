from rest_framework import generics
from .models import Beneficios
from .serializers import BeneficiosSerializer

class BeneficiosView(generics.RetrieveAPIView):
    queryset = Beneficios.objects.all()
    serializer_class = BeneficiosSerializer
    
    def get_object(self):
        instance, _ = Beneficios.objects.get_or_create(pk=1)
        return instance