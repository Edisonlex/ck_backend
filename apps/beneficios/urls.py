from django.urls import path
from .views import BeneficiosView

urlpatterns = [
    path('beneficios/', BeneficiosView.as_view(), name='beneficios'),
]