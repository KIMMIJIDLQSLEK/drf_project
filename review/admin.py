from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'product',
        'contents',
        'grade',
    )
    list_display_links = ('contents',)
    list_filter = ('product',)
    fieldsets = (
        ("info", {'fields': ('author', 'product', 'grade','contents')}),
        ('etc', {'fields': ('update_check', 'created_at',)}),
    )
    readonly_fields = ('update_check','created_at')

admin.site.register(Review,ReviewAdmin)

