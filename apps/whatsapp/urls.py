from django.urls import path
from .views import WhatsAppConfigView

urlpatterns = [
    path('whatsapp/', WhatsAppConfigView.as_view(), name='whatsapp'),
]