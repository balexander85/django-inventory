from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Item",
            {
                'fields': [
                    'name', 'description', 'value', 'insured', 'attachments'
                ]
            }
        ),
    ]

    list_display = (
        'id',
        'name',
        'description',
        'value',
        'insured',
        'last_updated',
        'admin_thumbnail'
    )
    search_fields = ['name']


admin.site.register(Item, ItemAdmin)
