from rest_framework import serializers
from .models import Review
from product.serializers import ProductSerializer


class ReviewSerializer(serializers.ModelSerializer):
    # product=ProductSerializer()

    #todo: review 생성(user context로 받아오기)
    def create(self,validated_data):
        review=Review(**validated_data)
        review.author=self.context['user']
        review.save()

        return review

    #todo: review 수정(grade,contents만 수정가능)
    def update(self,review,validated_data):
        for key,value in validated_data.items():
            if key=='grade':
                review.grade=value
            elif key=='contents':
                review.contents=value

        review.update_check=True
        review.save()
        return review


    class Meta:
        model=Review
        fields=['author','product','contents','grade','created_at','update_check']
        extra_kwargs={
            'author':{
                'read_only': True
            },
            'grade':{
                'error_messages':{
                    'required':'상품에 대한 평점을 남겨주세요.'
                }
            },
            'contents':{
                'error_messages':{
                    'required': '내용을 입력해주세요.'
                }
            },
            'created_at':{
                'read_only': True
            },
            'update_check':{
                'read_only': True
            }
        }