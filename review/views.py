from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CreateBlog(APIView):
    permissions=[permissions.IsAuthenticated]
    def post(self,request):
        user=request.user
        print(user)
        title=request.data['title']
        categories=request.data['category']
        contents=request.data['content']

        # #ToDo: 게시물 생성
        # article=Article.objects.create(
        #     author=user,
        #     title=title,
        #     contents=contents,
        # )
        #ToDo: 카테고리 등록
        # for category in categories:
        #     article.category.add(category)
        #     article.save()

        return Response({"message":"게시글 생성 완료"},status=status.HTTP_200_OK)

