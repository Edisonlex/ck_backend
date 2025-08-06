from django.contrib import admin
from .models import (
    ConfiguracionCursos,
    Curso,
    ObjetivoCurso,
    ModuloCurso,
    TemaModulo,
    RequisitoCurso,
    BeneficioCurso
)

class TemaModuloInline(admin.TabularInline):
    model = TemaModulo
    extra = 1
    fields = ('descripcion',)  # Solo mostrar el campo descripcion en el inline

class ModuloCursoInline(admin.TabularInline):
    model = ModuloCurso
    extra = 1
    show_change_link = True
    inlines = [TemaModuloInline]

class ObjetivoCursoInline(admin.TabularInline):
    model = ObjetivoCurso
    extra = 1

class RequisitoCursoInline(admin.TabularInline):
    model = RequisitoCurso
    extra = 1

class BeneficioCursoInline(admin.TabularInline):
    model = BeneficioCurso
    extra = 1

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nivel', 'modalidad', 'duracion', 'orden', 'destacado')
    list_editable = ('orden', 'destacado')
    list_filter = ('nivel', 'modalidad', 'destacado')
    search_fields = ('titulo', 'descripcion')
    inlines = [
        ObjetivoCursoInline,
        ModuloCursoInline,
        RequisitoCursoInline,
        BeneficioCursoInline
    ]
    fieldsets = (
        ('Información Básica', {
            'fields': (
                'titulo',
                'descripcion',
                ('nivel', 'duracion'),
                ('modalidad', 'certificacion'),
                ('color', 'icono_url'),
                ('estudiantes'),
                'orden',
                'destacado'
            )
        }),
    )

@admin.register(ConfiguracionCursos)
class ConfiguracionCursosAdmin(admin.ModelAdmin):
    list_display = ('titulo_seccion', )
    fieldsets = (
        ('Configuración General', {
            'fields': (
                ('titulo_seccion', 'descripcion_seccion'),
            )
        }),
    )
    
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

# Modelos registrados individualmente con configuraciones mejoradas
@admin.register(ObjetivoCurso)
class ObjetivoCursoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'curso')
    list_filter = ('curso',)
    search_fields = ('descripcion',)
    raw_id_fields = ('curso',)

@admin.register(RequisitoCurso)
class RequisitoCursoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'curso')
    list_filter = ('curso',)
    search_fields = ('descripcion',)
    raw_id_fields = ('curso',)

@admin.register(ModuloCurso)
class ModuloCursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'orden')
    list_filter = ('curso',)
    inlines = [TemaModuloInline]  # Aquí sí funcionará
    ordering = ('curso', 'orden')

@admin.register(BeneficioCurso)
class BeneficioCursoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'curso')
    list_filter = ('curso',)
    search_fields = ('descripcion',)
    raw_id_fields = ('curso',)

# Configuración corregida para TemaModulo
@admin.register(TemaModulo)
class TemaModuloAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'modulo')
    list_filter = ('modulo__curso', 'modulo')
    search_fields = ('descripcion',)
    raw_id_fields = ('modulo',)