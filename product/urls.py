from django.urls import path
from .views import ProductView,ProductImgView,ProductCreateView,ProductDetailView

urlpatterns=[
    path('',ProductView.as_view()),
    path('create/',ProductCreateView.as_view()),
    path('<obj_id>/',ProductDetailView.as_view()),
    path('img/<obj_id>/',ProductImgView.as_view()),  #이미지 url
]