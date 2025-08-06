from django.urls import path
from .views import ConfiguracionFAQView, PreguntasFrecuentesListView

urlpatterns = [
    path('config/', ConfiguracionFAQView.as_view(), name='faq-config'),
    path('preguntas/', PreguntasFrecuentesListView.as_view(), name='faq-preguntas'),
]