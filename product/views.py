from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class EventView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    #TODO
    #event 생성
    def post(self,request):
        #request: event모델
        event_serializer=EventSerializer(data=request.data)

        #validate
        event_serializer.is_valid(raise_exception=True)
        #create
        event_serializer.save()

        return Response(event_serializer.data,status=status.HTTP_200_OK)


