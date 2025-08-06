from rest_framework import generics
from .models import (
    ConfiguracionCursos,
    Curso,
    ObjetivoCurso,
    ModuloCurso,
    TemaModulo,
    RequisitoCurso,
    BeneficioCurso
)
from .serializers import (
    ConfiguracionCursosSerializer,
    CursoSerializer,
    ObjetivoCursoSerializer,
    ModuloCursoSerializer,
    TemaModuloSerializer,
    RequisitoCursoSerializer,
    BeneficioCursoSerializer
)

class ConfiguracionCursosView(generics.RetrieveAPIView):
    queryset = ConfiguracionCursos.objects.all()
    serializer_class = ConfiguracionCursosSerializer
    
    def get_object(self):
        instance, _ = ConfiguracionCursos.objects.get_or_create(pk=1)
        return instance

class CursoListView(generics.ListAPIView):
    serializer_class = CursoSerializer
    
    def get_queryset(self):
        return Curso.objects.filter(destacado=True).order_by('orden')

class CursoDetailView(generics.RetrieveAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    lookup_field = 'id'

class ObjetivoCursoCreateView(generics.CreateAPIView):
    queryset = ObjetivoCurso.objects.all()
    serializer_class = ObjetivoCursoSerializer

class ModuloCursoCreateView(generics.CreateAPIView):
    queryset = ModuloCurso.objects.all()
    serializer_class = ModuloCursoSerializer

class TemaModuloCreateView(generics.CreateAPIView):
    queryset = TemaModulo.objects.all()
    serializer_class = TemaModuloSerializer

class RequisitoCursoCreateView(generics.CreateAPIView):
    queryset = RequisitoCurso.objects.all()
    serializer_class = RequisitoCursoSerializer

class BeneficioCursoCreateView(generics.CreateAPIView):
    queryset = BeneficioCurso.objects.all()
    serializer_class = BeneficioCursoSerializer