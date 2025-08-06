from django.urls import path
from .views import CallToActionView

urlpatterns = [
    path('contacto/', CallToActionView.as_view(), name='contacto'),
]