from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Article,Category

# Create your views here.
class CreateBlog(APIView):
    permissions=[permissions.IsAuthenticated]
    def post(self,request):
        user=request.user
        title=request.data.get('title')
        categories=request.data.get('category')
        contents=request.data.get('content')
        Article.objects.create(
            author=user,
            title=title,
            contents=contents,
        )
        # for category in categories:
        #     category_name=Category.objects.get(name=category)



        return Response({"message":"게시글 생성 완료"},status=status.HTTP_200_OK)

