from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField("이벤트 제목",max_length=100)
    preview=models.CharField("미리보기",max_length=100)
    introduction=models.CharField("설명",max_length=200)
    created_at=models.DateField("등록일자",auto_now_add=True)
    started_at=models.DateField("노출시작일",auto_now=True)
    ended_at=models.DateField("노출종료일",auto_now=True)
    activate=models.BooleanField("활성화여부")

