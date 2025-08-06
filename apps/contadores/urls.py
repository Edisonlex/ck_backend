from django.urls import path
from .views import ContadorAPIView

urlpatterns = [
    path('counter-section/', ContadorAPIView.as_view(), name='counter-section'),
]