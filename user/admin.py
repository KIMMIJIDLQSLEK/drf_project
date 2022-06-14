from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User,UserProfile

#Group빼기
admin.site.unregister(Group)

class UserAdmin(admin.ModelAdmin):
    list_display=['id','username']

#user모델 등록
admin.site.register(User,UserAdmin)
admin.site.register(UserProfile)