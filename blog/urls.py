from django.urls import path
from .views import CreateBlog


urlpatterns=[
    path('blog/',CreateBlog.as_view()),
]