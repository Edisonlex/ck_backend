from django.urls import path
from .views import GaleriaConfigView, GaleriaListView

urlpatterns = [
    path('galeria/config/', GaleriaConfigView.as_view(), name='galeria-config'),
    path('galeria/', GaleriaListView.as_view(), name='galeria-list'),
]