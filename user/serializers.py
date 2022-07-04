from rest_framework import serializers
from .models import User,UserProfile
from blog.models import Article,Category

#ToDo
#UserProfileSerializer생성
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=["introduction"]

#ToDo: 회원가입+소개글작성
#UserSerializer생성
class UserSerializer(serializers.ModelSerializer):
    userprofile=UserProfileSerializer()

    # custom creator
    def create(self, validated_data):
        user_profile=validated_data.pop('userprofile')

        #User object 생성
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        #UserProfile object 생성
        UserProfile.objects.create(user=user,**user_profile)

        return user

    class Meta:
        model=User
        fields=["username","password","email","nickname",'is_seller',"userprofile"]


        extra_kwargs={
            'password':{'write_only':True},
        }
