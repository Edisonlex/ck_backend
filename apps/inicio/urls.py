from django.urls import path
from .views import HeroSectionUpdateAPIView

urlpatterns = [
    path('hero-section/', HeroSectionUpdateAPIView.as_view(), name='hero-section'),
]