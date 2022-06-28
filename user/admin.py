from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User,UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Group빼기
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    #UserAdmin을 사용할시 필수!
    list_display = ("id","username", "password","email", "nickname", "is_active")
    list_filter = ("username",)
    filter_horizontal = []

    #선택
    list_display_links = ('username',)
    readonly_fields = ('created_at',)
    fieldsets = (
        ('info',{'fields':('username','password','email','nickname','created_at')}),
        ('permissions',{'fields':('is_active','is_admin')})
    )



#user모델 등록
admin.site.register(User,UserAdmin)
admin.site.register(UserProfile)