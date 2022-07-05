from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'product',
        'contents',
        'grade'
    )
    list_display_links = ('product',)
    readonly_fields = ('created_at',)

admin.site.register(Review,ReviewAdmin)

