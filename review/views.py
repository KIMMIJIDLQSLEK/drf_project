from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer

# Create your views here.
class ReviewGetOrCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    #Todo: reviews 조회(전부)
    def get(self,request):
        reviews=Review.objects.all()
        review_serializer=ReviewSerializer(reviews,many=True)

        return Response(review_serializer.data,status=status.HTTP_200_OK)

    #Todo: review 생성
    def post(self,request):
        user=request.user
        review_serializer=ReviewSerializer(data=request.data,context={'user':user})

        #검증
        review_serializer.is_valid(raise_exception=True)

        #생성
        review_serializer.save()

        return Response(review_serializer.data,status=status.HTTP_200_OK)


class ReviewUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    #TODO: review 수정
    def post(self,request,obj_id):
        review=Review.objects.get(id=obj_id)
        print(review)
        if request.user==review.author:
            review_serializer=ReviewSerializer(review,data=request.data,partial=True)

           # 검증
            review_serializer.is_valid(raise_exception=True)
            #수정
            review_serializer.save()

            return Response(review_serializer.data,status=status.HTTP_200_OK)

        #리뷰작성자가 아닐경우
        return Response({'error':'리뷰의 작성자가 아닙니다.'},status=status.HTTP_400_BAD_REQUEST)


