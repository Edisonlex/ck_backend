from django.contrib import admin
from .models import CallToAction
from django.forms import ModelChoiceField

@admin.register(CallToAction)
class CallToActionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'whatsapp')

    fieldsets = (
        ('Configuración General', {
            'fields': (
                'titulo',
                'descripcion',
                'ubicacion',
            )
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'ubicacion':
            field.label = 'Teléfono'
        return field
