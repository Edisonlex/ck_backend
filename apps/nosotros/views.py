from rest_framework import generics
from .models import InformacionInstitucional
from .serializers import InformacionInstitucionalSerializer

class InformacionInstitucionalView(generics.RetrieveAPIView):
    queryset = InformacionInstitucional.objects.all()
    serializer_class = InformacionInstitucionalSerializer
    
    def get_object(self):
        instance, _ = InformacionInstitucional.objects.get_or_create(pk=1)
        return instance