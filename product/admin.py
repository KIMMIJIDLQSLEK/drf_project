from django.contrib import admin
from .models import Product,Category
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'product_name',
        'price',
        'started_at',
        'ended_at',
        'img_preview'
    )
    list_display_links = ('product_name',)

    def img_preview(self,obj):
        return mark_safe(f'<img src="/products/img/{obj.id}/" height="150px"/>')

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'introduction'
    )

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
