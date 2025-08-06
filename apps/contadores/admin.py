from django.contrib import admin
from .models import Contador

@admin.register(Contador)
class ContadorAdmin(admin.ModelAdmin):
    list_display = ('años_experiencia', 'estudiantes_graduados', 'programas_academicos', 'docentes_expertos')
    fieldsets = (
        ('Estadísticas', {
            'fields': (
                ('años_experiencia', 'estudiantes_graduados'),
                ('programas_academicos', 'docentes_expertos')
            )
        }),
    )
    
    def has_add_permission(self, request):
        # Limitar a una sola instancia
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)