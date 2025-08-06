from django.contrib import admin
from .models import ConfiguracionGaleria, GaleriaImagen
from django.utils.html import format_html

@admin.register(ConfiguracionGaleria)
class ConfiguracionGaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo_seccion',)
    fieldsets = (
        ('Configuración General', {
            'fields': (
                ('titulo_seccion', 'descripcion_seccion'),
            )
        }),
    )
    
    def has_add_permission(self, request):
        # Limitar a una sola instancia
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(GaleriaImagen)
class GaleriaImagenAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen_preview', 'orden', 'destacada')
    list_editable = ('orden', 'destacada')
    list_filter = ('destacada',)
    search_fields = ('titulo', 'descripcion')
    
    def imagen_preview(self, obj):
        if obj.imagen_url:  # ← Cambio clave aquí
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />', 
                obj.imagen_url  # Usamos la URL directamente
            )
        return "-"
    
    imagen_preview.short_description = 'Vista Previa'