from django.urls import path
from .views import InformacionInstitucionalView

urlpatterns = [
    path('informacion/', InformacionInstitucionalView.as_view(), name='informacion-institucional'),
]

