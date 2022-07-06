from django.urls import path
from .views import ProductView,ProductImgView

urlpatterns=[
    path('',ProductView.as_view()),
    #이메일 url
    path('img/<obj_id>/',ProductImgView.as_view()),
]