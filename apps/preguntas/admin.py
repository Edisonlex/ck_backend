from django.contrib import admin
from .models import ConfiguracionFAQ, PreguntaFrecuente

@admin.register(ConfiguracionFAQ)
class ConfiguracionFAQAdmin(admin.ModelAdmin):
    list_display = ('titulo_seccion', )
    fieldsets = (
        ('Configuración General', {
            'fields': (
                ('titulo_seccion', 'descripcion_seccion'),
            )
        }),
        ('Información de Contacto', {
            'fields': (
                'whatsapp',
                'email',
            )
        }),
    )
    
    def has_add_permission(self, request):
        # Limitar a una sola instancia
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

@admin.register(PreguntaFrecuente)
class PreguntaFrecuenteAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'orden')
    list_editable = ('orden',)
    search_fields = ('pregunta', 'respuesta')
    list_per_page = 20