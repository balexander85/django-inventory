from django.contrib import admin
from .models import Item, ItemType, ItemAttachment


class ItemAttachmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "ItemType",
            {
                'fields': ['name', 'attachment', 'item']
            }
        ),
    ]

    list_display = ('name', 'item')
    search_fields = ['name']


class ItemAttachmentInline(admin.TabularInline):
    model = ItemAttachment


class ItemTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "ItemType",
            {
                'fields': ['name', ]
            }
        ),
    ]

    list_display = ('id', 'name',)
    search_fields = ['name']


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Item",
            {
                'fields': [
                    'name',
                    'description',
                    'value',
                    'insured',
                    'profile_image',
                    'item_type',
                ]
            }
        ),
    ]

    inlines = [
        ItemAttachmentInline,
    ]

    list_display = (
        'id',
        'name',
        'description',
        'value',
        'insured',
        'last_updated',
        'item_type',
        'admin_thumbnail',
        'attachments',
    )
    search_fields = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
# admin.site.register(ItemAttachment, ItemAttachmentAdmin)
