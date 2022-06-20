from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework import status
from .models import User,UserProfile
from blog.models import Article

# Create your views here.
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        username=request.data.get('username','')
        password=request.data.get('password','')
        email=request.data.get('email','')

        user=authenticate(request,username=username,password=password,email=email)
        if not user:
            return Response({"message":"존재하지 않는 계정이거나 아이디와 비밀번호가 일치하지 않습니다."},status=status.HTTP_401_UNAUTHORIZED)

        login(request,user)
        return Response({"message":"로그인완료"},status=status.HTTP_200_OK)

class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request):
        user=User.objects.get(pk=2)
        print(user)
        if user.is_authenticated: #user가 존재하면
            userprofile=UserProfile.objects.get(user=user)
            article=Article.objects.get(author=user)

            data={
                "nickname":userprofile.user.nickname,
                "introduction":userprofile.introduction,
                "title":article.title,
                "contents":article.contents,

            }
            return Response(data,status=status.HTTP_200_OK)

        else:
            return Response({"message":"로그인을 해주세요"},status=status.HTTP_401_UNAUTHORIZED)


