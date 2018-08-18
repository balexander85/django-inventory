from django.db import models
from django.utils.safestring import mark_safe


class Item(models.Model):
    name = models.CharField(max_length=50)
    insured = models.BooleanField(default=False)
    description = models.CharField(max_length=500, default='', blank=True)
    value = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    attachments = models.ImageField(
        'Image', upload_to='images/%Y/%m', null=True, blank=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def admin_thumbnail(self):
        return mark_safe(
            f'<a href="{self.attachments.url}">'
            f'<img src="{self.attachments.url}" width="150" height="150" />'
            f'</a>'
        )

    admin_thumbnail.short_description = 'Image'
