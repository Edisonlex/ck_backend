from django.contrib import admin
from .models import Ubicacion

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo_seccion', 'telefono', 'email')
    fieldsets = (
        ('Configuración General', {
            'fields': (
                ('titulo_seccion', 'descripcion_seccion'),
                'mapa_embed',
            )
        }),
        ('Información de Contacto', {
            'fields': (
                'direccion',
                'horarios',
                ('telefono', 'email'),
                'como_llegar',
            )
        }),
    )
    
    def has_add_permission(self, request):
        # Limitar a una sola instancia
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)