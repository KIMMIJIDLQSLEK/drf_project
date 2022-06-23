from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField("카테고리 이름", max_length=100)
    introduction=models.TextField("설명")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Categories'

class Article(models.Model):
    author=models.ForeignKey(to=User,verbose_name="글작성자",on_delete=models.CASCADE) #user와 일대다관계
    title=models.CharField("글제목",max_length=50)
    category=models.ManyToManyField(to=Category,verbose_name="카테고리") #category와 다대다관계
    contents=models.TextField("글내용")
    created_at=models.DateField("작성날짜",auto_now_add=True)

    def __str__(self):
        return f"{self.author}의 게시물: {self.title}"