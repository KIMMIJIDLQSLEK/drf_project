from rest_framework import serializers
from .models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','introduction']


class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerializer(many=True,read_only=True) #직렬화할때 사용
    get_categories = serializers.ListField(required=False) #값을 리스트형태로 받을때

    #TODO: product 생성(user context로 받아오기)
    def create(self,validated_data):
        #카테고리
        categories=list(map(int,validated_data.pop('get_categories')[0].split(",")))

        #Product object 생성
        product=Product(**validated_data)

        #user 등록
        product.user=self.context['user']
        product.save()

        #category 등록
        product.category.add(*categories)
        product.save()

        return product


    #TODO: 시작일<=종료일
    #custom validator
    def validate(self,data):
        if data.get("started_at",0)>data.get("ended_at",0):
            raise serializers.ValidationError(
                detail={"error":"노출종료일이 노출시작일보다 빠릅니다."}
            )
        return data

    class Meta:
        model=Product
        fields=['product_name','product_img','price','started_at','ended_at','category','get_categories']  #product_img 추가
        extra_kwargs={
            'product_name':{
                'error_messages':{
                    'required':'상품명을 입력해주세요.',
                }
            },
            'product_img':{
                'error_messages':{
                    'invalid':'상품이미지를 반드시 등록해주세요.',
                }
            },
            'started_at':{
                'error_messages':{
                    'required':'시작일을 입력해주세요.',
                    'invalid':'날짜 형식이 아닙니다.',
                }
            },
            'ended_at': {
                'error_messages': {
                    'required': '종료일을 입력해주세요.',
                    'invalid': '날짜 형식이 아닙니다.',
                }
            },
        }

