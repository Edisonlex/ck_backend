from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse


urlpatterns = [
    path('admin/', admin.site.urls),
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)