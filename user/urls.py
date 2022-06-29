from django.urls import path
from .views import SignInView,UserView


urlpatterns=[
    path('signin/',SignInView.as_view()), #로그인기능
    path('',UserView.as_view()),
]