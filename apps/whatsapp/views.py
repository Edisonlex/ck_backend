from rest_framework.generics import RetrieveAPIView
from .models import WhatsAppConfig
from .serializers import WhatsAppConfigSerializer

class WhatsAppConfigView(RetrieveAPIView):
    queryset = WhatsAppConfig.objects.all()
    serializer_class = WhatsAppConfigSerializer

    def get_object(self):
        return WhatsAppConfig.objects.first()  # retorna la única instancia
