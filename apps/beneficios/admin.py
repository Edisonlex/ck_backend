from django.contrib import admin
from .models import Beneficios

@admin.register(Beneficios)
class BeneficiosAdmin(admin.ModelAdmin):
    list_display = ('titulo_seccion',)
    fieldsets = (
        ('Configuración de la sección', {
            'fields': (
                ('titulo_seccion', 'subtitulo_seccion'),
            )
        }),
        ('Beneficio 1', {
            'fields': (
                ('beneficio1_titulo', 'beneficio1_descripcion'),
            )
        }),
        ('Beneficio 2', {
            'fields': (
                ('beneficio2_titulo', 'beneficio2_descripcion'),
            )
        }),
        ('Beneficio 3', {
            'fields': (
                ('beneficio3_titulo', 'beneficio3_descripcion'),
            )
        }),
        ('Beneficio 4', {
            'fields': (
                ('beneficio4_titulo', 'beneficio4_descripcion'),
            )
        }),
    )
    
    def has_add_permission(self, request):
        # Limitar a una sola instancia
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)