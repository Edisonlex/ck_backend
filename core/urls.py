from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.routers import DefaultRouter

# from apps.cursos.views import CursoViewSet
# from apps.ubicacion.views import UbicacionViewSet
# from apps.beneficios.views import BeneficiosViewSet

# ruta = DefaultRouter()
# ruta.register(r'cursos', CursoViewSet)
# ruta.register(r'ubicacion', UbicacionViewSet)
# ruta.register(r'beneficios', BeneficiosViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(ruta.urls)),
    path('api/', include('apps.inicio.urls')),
    path('api/', include('apps.contadores.urls')),
    path('api/', include('apps.nosotros.urls')),
    path('api/', include('apps.beneficios.urls')),
    path('api/', include('apps.galeria.urls')),
    path('api/', include('apps.ubicacion.urls')),
    path('api/', include('apps.preguntas.urls')),
    path('api/', include('apps.contacto.urls')),
    path('api/', include('apps.whatsapp.urls')),
    path('api/', include('apps.cursos.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
