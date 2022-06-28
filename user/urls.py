from django.urls import path
from .views import LoginView,UserView


urlpatterns=[
    path('',UserView.as_view()),
    path('login/',LoginView.as_view()),
]