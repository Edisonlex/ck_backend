from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

# Añade esta función para la ruta raíz
def api_home(request):
    return JsonResponse({
        'status': 'ok',
        'message': 'API de Fundación CK funcionando correctamente',
        'endpoints': [
            '/api/',
            '/admin/'
        ]
    })

urlpatterns = [
    # Añade esta línea para la ruta raíz
    path('', api_home, name='api_home'),
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

# Modifica esta parte para que los archivos estáticos funcionen en producción
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)