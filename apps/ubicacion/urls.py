from django.urls import path
from .views import UbicacionView

urlpatterns = [
    path('ubicacion/', UbicacionView.as_view(), name='ubicacion'),
]