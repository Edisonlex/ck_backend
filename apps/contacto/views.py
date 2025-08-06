from rest_framework import generics
from .models import CallToAction
from .serializers import CallToActionSerializer

class CallToActionView(generics.RetrieveAPIView):
    queryset = CallToAction.objects.all()
    serializer_class = CallToActionSerializer
    
    def get_object(self):
        instance, _ = CallToAction.objects.get_or_create(pk=1)
        return instance