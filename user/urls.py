from django.urls import path
from .views import LoginView,UserView


urlpatterns=[
    path('signin/',LoginView.as_view()), #로그인기능
    path('',UserView.as_view()),
]