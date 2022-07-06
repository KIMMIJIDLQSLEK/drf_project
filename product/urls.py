from django.urls import path
from .views import ProductView,ProductImgView,ProductCreateView

urlpatterns=[
    path('',ProductView.as_view()),
    #이메일 url
    path('create/',ProductCreateView.as_view()),
    path('img/<obj_id>/',ProductImgView.as_view()),
]