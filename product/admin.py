from django.contrib import admin
from .models import Event,Product
from django.utils.safestring import mark_safe

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'thumbnail',
        'introduction',
        'started_at',
        'ended_at',
        'activate',
        'thumbnail_preview'
    )

    def thumbnail_preview(self,obj):
        return mark_safe(f'<img src="/product/thumbnail/{obj.id}/" height="150px"/>')



# Register your models here.
admin.site.register(Event,EventAdmin)
admin.site.register(Product)
