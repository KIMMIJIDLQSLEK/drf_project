from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

#Group빼기
admin.site.unregister(Group)

#user모델 등록
admin.site.register(User)