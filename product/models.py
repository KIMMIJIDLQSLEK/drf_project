from django.db import models
from user.models import User

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

class Category(models.Model):
    name=models.CharField("카테고리 이름", max_length=100)
    introduction=models.TextField("설명")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Categories'

class Product(models.Model):
    product_name=models.CharField("상품이름",max_length=100)
    product_img=models.ImageField("상품이미지",upload_to='images/product/',blank=True)
    category=models.ManyToManyField(to=Category,verbose_name="카테고리")
    price=models.IntegerField("가격")
    uploaded_at=models.DateField("상품업로드날짜",auto_now_add=True)

    def __str__(self):
        return self.product_name

