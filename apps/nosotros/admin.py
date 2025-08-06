from django.contrib import admin
from .models import InformacionInstitucional

@admin.register(InformacionInstitucional)
class InformacionInstitucionalAdmin(admin.ModelAdmin):
    list_display = ('titulo_principal', 'años_experiencia')
    fieldsets = (
        ('Información Principal', {
            'fields': (
                'titulo_principal',
                'descripcion_principal',
                'años_experiencia'
            ),
        }),
        ('Misión', {
            'fields': (
                'mision_titulo',
                'mision_descripcion',
            ),
        }),
        ('Visión', {
            'fields': (
                'vision_titulo',
                'vision_descripcion',
            ),
        }),
    )
    
    def has_add_permission(self, request):
        # Limitar a una sola instancia
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)