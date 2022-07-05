from django.urls import path
from .views import ProductAllView,ProductImgView

urlpatterns=[
    path('',ProductAllView.as_view()),
    #이메일 url
    path('img/<obj_id>/',ProductImgView.as_view()),
]