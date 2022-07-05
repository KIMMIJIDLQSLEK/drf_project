from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework import status
from .serializers import UserSerializer

# Create your views here.
#todo: 로그인 기능
class SignInView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        username=request.data.get('username','')
        password=request.data.get('password','')
        email=request.data.get('email','')

        user=authenticate(request,username=username,password=password,email=email)
        if not user:
            return Response({"message":"존재하지 않는 계정이거나 아이디와 비밀번호가 일치하지 않습니다."},status=status.HTTP_401_UNAUTHORIZED)

        login(request,user)
        return Response({"message":f"{user.username}님, 로그인완료"},status=status.HTTP_200_OK)


#todo: 회원가입기능
class SignUpView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        user_serializer=UserSerializer(data=request.data)

        #검증
        user_serializer.is_valid(raise_exception=True)
        #생성
        user_serializer.save()

        return Response(user_serializer.data,status=status.HTTP_200_OK)


#todo: 마이페이지 기능
class MyPageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user=request.user
        user_serializer_data=UserSerializer(user).data

        return Response(user_serializer_data["userprofile"],status=status.HTTP_200_OK)

