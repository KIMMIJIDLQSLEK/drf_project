from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    #TODO: 시작일<=종료일
    #custom validator
    def validate(self,data):
        if data.get("started_at",0)>data.get("ended_at",0):
            raise serializers.ValidationError(
                detail={"error":"노출종료일이 노출시작일보다 빠릅니다."}
            )
        return data

    class Meta:
        model=Event
        fields=['title','preview','introduction','started_at','ended_at','activate']
        extra_kwargs={
            'title':{
                'error_messages':{
                    'required':'제목을 입력해주세요.',
                }
            },
            'started_at':{
                'error_messages':{
                    'required':'시작일을 입력해주세요.',
                    'invalid':'날짜 또는 시간 형식이 아닙니다.',
                }
            },
            'ended_at': {
                'error_messages': {
                    'required': '종료일을 입력해주세요.',
                    'invalid': '날짜 또는 시간 형식이 아닙니다.',
                }
            }
        }

