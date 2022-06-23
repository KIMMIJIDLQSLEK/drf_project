from rest_framework import serializers
from .models import User,UserProfile
from blog.models import Article,Category

#TODO
#ArticleSerializer생성
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=["title","contents"]

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
    article_set=ArticleSerializer(many=True)

    class Meta:
        model=User
        fields=["username","password","email","nickname","userprofile","article_set"]

        extra_kwargs={
            'password':{'write_only':True}
        }
