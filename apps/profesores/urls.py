from django.urls import path
from .views import (
    ConfiguracionProfesoresView,
    ProfesorListView,
    ProfesorDetailView,
)

urlpatterns = [
    path('profesor/config/', ConfiguracionProfesoresView.as_view(), name='configuracion-profesores'),
    path('profesor/', ProfesorListView.as_view(), name='profesor-list'),
    path('profesor/<int:id>/', ProfesorDetailView.as_view(), name='profesor-detail'),

]