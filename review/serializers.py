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


    class Meta:
        model=Review
        fields=['author','product','contents','grade']
        extra_kwargs={
            'author':{
                'required':False
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
            }
        }