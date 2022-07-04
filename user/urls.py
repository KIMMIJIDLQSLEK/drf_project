from django.urls import path
from .views import SignInView,SignUpView,MyPageView


urlpatterns=[
    path('signin/',SignInView.as_view()), #로그인기능
    path('signup/',SignUpView.as_view()), #회원가입기능
    path('mypage/',MyPageView.as_view()), #마이페이지기능
]