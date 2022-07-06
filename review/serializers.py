from rest_framework import serializers
from .models import Review
from product.serializers import ProductSerializer


class ReviewSerializer(serializers.ModelSerializer):
    # product=ProductSerializer()
    class Meta:
        model=Review
        fields=['id','author','product','contents','grade']