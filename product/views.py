import os.path

from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from django.views.static import serve
from datetime import datetime
from django.db.models import Q
from rest_framework import permissions

#todo: permission 커스텀(seller & isauthenticated)
class SellerPermissision(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_seller
        )


class ProductView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    #TODO: products 조회(오늘날짜가 상품노출시작일자와 상품노출끝일자 사이인 상품 불러오기)
    def get(self,request):
        today=datetime.now().date()
        products=Product.objects.filter(
            Q(started_at__lte=today)&Q(ended_at__gte=today)
        )

        product_serializer=ProductSerializer(products,many=True)

        return Response(product_serializer.data,status=status.HTTP_200_OK)

class ProductCreateView(APIView):
    permission_classes =[SellerPermissision]

    #TODO: product 생성
    def post(self,request):
        #request: product모델
        user=request.user
        product_serializer=ProductSerializer(data=request.data,context={'user': user})

        #validate
        product_serializer.is_valid(raise_exception=True)
        #create
        product_serializer.save()

        return Response(product_serializer.data,status=status.HTTP_200_OK)

class ProductDetailView(APIView):
    permissions_classes=[permissions.IsAuthenticated]

    #TODO: product detail 조회
    def get(self,request,obj_id):
        product=Product.objects.get(id=obj_id)
        product_serializer=ProductSerializer(product)

        return Response(product_serializer.data,status=status.HTTP_200_OK)


    #TODO: product detail 수정
    def post(self,request,obj_id):
        user=request.user
        product=Product.objects.get(id=obj_id)
        if user.is_seller is False and product.user!=user: #판매자가 아닐경우
            return Response({'error':'해당하는 상품의 판매자가아닙니다.'},status=status.HTTP_400_BAD_REQUEST)

        product_serializer=ProductSerializer(product,data=request.data,partial=True)

        #검증
        product_serializer.is_valid(raise_exception=True)
        #수정
        product_serializer.save()

        return Response(product_serializer.data,status=status.HTTP_200_OK)


class ProductImgView(APIView):
    #TODO
    #get으로 ProductImg 링크 가져오기
    def get(self,request,obj_id):
        #1.Product모델 가져오기
        #2.Product모델의 썸네일 경로 가져오기
        #3.경로 보내기
        product=Product.objects.get(id=obj_id)
        productimg_path=product.product_img.path
        return serve(request,os.path.basename(productimg_path),os.path.dirname(productimg_path))




