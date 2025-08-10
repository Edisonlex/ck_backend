from django.contrib import admin
from django.utils.html import format_html
from .models import Profesor, ConfiguracionProfesores


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de profesores
    list_display = ('nombre_completo', 'titulo', 'especialidad', 'experiencia_años', 'mostrar_cursos', 'imagen_preview')
    # Campos por los que se puede filtrar
    list_filter = ('especialidad', 'cursos_dictados')
    # Campos por los que se puede buscar
    search_fields = ('nombre', 'apellido', 'titulo', 'especialidad')
    # Campos editables directamente en la lista
    list_editable = ('titulo', 'especialidad')
    # Para seleccionar múltiples cursos con un widget mejorado
    filter_horizontal = ('cursos_dictados',)
    
    # Campos para el formulario de edición
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'foto', 'color')
        }),
        ('Información Profesional', {
            'fields': ('titulo', 'especialidad', 'descripcion', 'experiencia_años')
        }),
        ('Cursos', {
            'fields': ('cursos_dictados',)
        }),
    )

    # Para mostrar los cursos como string en la lista
    def mostrar_cursos(self, obj):
        return ", ".join([curso.titulo for curso in obj.cursos_dictados.all()])
    mostrar_cursos.short_description = 'Cursos que dicta'
    
    # Vista previa de la imagen
    def imagen_preview(self, obj):
        if obj.foto:  # Asumiendo que foto contiene una URL como string
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />', 
                obj.foto  # Usamos directamente el string con la URL
            )
        return "-"
    imagen_preview.short_description = 'Vista Previa'


@admin.register(ConfiguracionProfesores)
class ConfiguracionProfesoresAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion_corta')
    
    def descripcion_corta(self, obj):
        """Muestra una versión acortada de la descripción en el listado"""
        return f"{obj.descripcion[:50]}..." if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = "Descripción"
    
    def has_add_permission(self, request):
        """Limita a solo una instancia de configuración"""
        if ConfiguracionProfesores.objects.exists():
            return False
        return super().has_add_permission(request)
    
    # Opcional: descomentar para evitar eliminar la configuración
    # def has_delete_permission(self, request, obj=None):
    #     return False