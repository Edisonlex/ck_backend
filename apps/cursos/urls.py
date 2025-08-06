from django.urls import path
from .views import (
    ConfiguracionCursosView,
    CursoListView,
    CursoDetailView,
    ObjetivoCursoCreateView,
    ModuloCursoCreateView,
    TemaModuloCreateView,
    RequisitoCursoCreateView,
    BeneficioCursoCreateView
)

urlpatterns = [
    # Configuración
    path('cursos/config/', ConfiguracionCursosView.as_view(), name='cursos-config'),
    
    # Cursos
    path('cursos/', CursoListView.as_view(), name='cursos-list'),
    path('cursos/<str:id>/', CursoDetailView.as_view(), name='curso-detail'),
    
    # Relaciones
    path('objetivos/', ObjetivoCursoCreateView.as_view(), name='objetivo-create'),
    path('modulos/', ModuloCursoCreateView.as_view(), name='modulo-create'),
    path('temas/', TemaModuloCreateView.as_view(), name='tema-create'),
    path('requisitos/', RequisitoCursoCreateView.as_view(), name='requisito-create'),
    path('beneficios/', BeneficioCursoCreateView.as_view(), name='beneficio-create'),
]