import os.path

from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from django.views.static import serve

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

class EventThumbnailView(APIView):
    permission_classes = []
    #TODO
    #get으로 EventThumbnail 링크 가져오기
    def get(self,request,obj_id):
        #1.Event모델 가져오기
        #2.Event모델의 썸네일 경로 가져오기
        #3.경로 보내기
        event=Event.objects.get(id=obj_id)
        thumbnail_path=event.thumbnail.path
        return serve(request,os.path.basename(thumbnail_path),os.path.dirname(thumbnail_path))



