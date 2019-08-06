from django.db import models
from django.utils.safestring import mark_safe


class ItemType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    insured = models.BooleanField(default=False)
    description = models.CharField(max_length=500, default="", blank=True)
    value = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    profile_image = models.ImageField(
        "image", upload_to="images/%Y/%m", null=True, blank=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def admin_thumbnail(self):
        if self.profile_image:
            image_url = self.profile_image.url
            return mark_safe(
                f'<a href="{image_url}">'
                f'<img src="{image_url}" width="150" height="150" />'
                f"</a>"
            )

    admin_thumbnail.short_description = "Profile Image"

    def attachments(self):
        return mark_safe(
            "<br />".join(
                [
                    f'<a href="{x.attachment.url}">{x}</a>'
                    for x in self.itemattachment_set.model.objects.all()
                    if x.item_id == self.id
                ]
            )
        )


class ItemAttachment(models.Model):
    name = models.CharField(max_length=20)
    attachment = models.FileField(
        "Attachment", upload_to="files/%Y/%m", null=True, blank=True
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
