from django.contrib import admin
from .models import WhatsAppConfig

@admin.register(WhatsAppConfig)
class WhatsAppConfigAdmin(admin.ModelAdmin):
    list_display = ('whatsapp', 'mensaje_predeterminado')  # usa la propiedad correctamente

    fieldsets = (
        ('Configuración General', {
            'fields': (
                'ubicacion',  # este es el campo real
                'mensaje_predeterminado',
            )
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'ubicacion':
            field.label = 'Teléfono'
        return field
