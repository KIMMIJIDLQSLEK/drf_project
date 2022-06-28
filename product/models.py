from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField("이벤트 제목",max_length=100)
    thumbnail=models.ImageField("썸네일",upload_to='images/product/',blank=True)
    introduction=models.CharField("설명",max_length=200)
    created_at=models.DateField("등록일자",auto_now_add=True)
    started_at=models.DateTimeField("노출시작일",)
    ended_at=models.DateTimeField("노출종료일")
    activate=models.BooleanField("활성화여부")

    def __str__(self):
        return f"{self.title}/({self.activate})"