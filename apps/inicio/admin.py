from django.contrib import admin
from django.utils.html import format_html
from .models import HeroSection

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'background_preview', 'badge_text', 'subtitle')
    list_editable = ('badge_text', 'subtitle')
    list_filter = ('badge_text',)
    search_fields = ('title', 'subtitle', 'description')
    
    def background_preview(self, obj):
        if obj.background_image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px; object-fit: cover;" />',
                obj.background_image
            )
        return "-"
    
    background_preview.short_description = 'Fondo'
    
    def has_add_permission(self, request):
        # Limitar a una sola instancia
        return HeroSection.objects.count() < 1
    
    # Opcional: Deshabilitar eliminación si solo hay un registro
    def has_delete_permission(self, request, obj=None):
        return HeroSection.objects.count() > 1