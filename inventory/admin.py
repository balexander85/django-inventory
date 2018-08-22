import csv

from django.contrib import admin
from django.http import HttpResponse
from .models import Item, ItemType, ItemAttachment


class ExportCsvMixin:

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = 'Export Selected'


class ItemAttachmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'ItemType',
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
            'ItemType',
            {
                'fields': ['name', ]
            }
        ),
    ]

    list_display = ('id', 'name',)
    search_fields = ['name']


class ItemAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ['export_as_csv']
    fieldsets = [
        (
            'Item',
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
    inlines = [ItemAttachmentInline,]
    list_display = (
        'name',
        'description',
        'value',
        'insured',
        'last_updated',
        'item_type',
        'admin_thumbnail',
        'attachments',
    )
    ordering = ['id']
    search_fields = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
# admin.site.register(ItemAttachment, ItemAttachmentAdmin)
