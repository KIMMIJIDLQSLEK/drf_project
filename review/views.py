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

