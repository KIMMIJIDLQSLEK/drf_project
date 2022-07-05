from django.urls import path
from .views import CreateBlog


urlpatterns=[
    path('create/',CreateBlog.as_view()),
]