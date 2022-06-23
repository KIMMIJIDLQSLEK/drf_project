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
    author=models.ForeignKey(to=User,verbose_name="게시물작성자",on_delete=models.CASCADE) #user와 일대다관계
    title=models.CharField("게시물 제목",max_length=50)
    category=models.ManyToManyField(to=Category,verbose_name="게시물 카테고리") #category와 다대다관계
    contents=models.TextField("게시물 내용")
    created_at=models.DateField("게시물작성날짜",auto_now_add=True)

    def __str__(self):
        return f"{self.author}의 게시물: {self.title}"

class Comment(models.Model):
    article=models.ForeignKey(to=Article,verbose_name="게시물",on_delete=models.CASCADE)
    author=models.ForeignKey(to=User,verbose_name="댓글작성자",on_delete=models.CASCADE)
    contents=models.CharField("댓글",max_length=100)
    created_at=models.DateField("댓글작성날짜",auto_now_add=True)

    def __str__(self):
        return f"{self.article}-{self.author}의 댓글"