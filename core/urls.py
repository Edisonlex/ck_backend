from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

# Agrupa todas las URLs de las apps en un archivo urls.py separado
# o usa un include que apunte a cada app con un prefijo
api_patterns = [
    path('', include('apps.inicio.urls')),
    path('', include('apps.contadores.urls')),
    path('', include('apps.nosotros.urls')),
    path('', include('apps.beneficios.urls')),
    path('', include('apps.galeria.urls')),
    path('', include('apps.ubicacion.urls')),
    path('', include('apps.preguntas.urls')),
    path('', include('apps.contacto.urls')),
    path('', include('apps.whatsapp.urls')),
    path('', include('apps.cursos.urls')),
    path('', include('apps.profesores.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)