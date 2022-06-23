from rest_framework import serializers
from .models import User,UserProfile
from blog.models import Article,Category

#ToDo
#UserProfileSerializer생성
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=["introduction"]

#ToDo
#UserSerializer생성
class UserSerializer(serializers.ModelSerializer):
    userprofile=UserProfileSerializer()

    class Meta:
        model=User
        fields=["username","password","email","nickname","userprofile"]

        extra_kwargs={
            'password':{'write_only':True}
        }
