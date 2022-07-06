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

class Product(models.Model):
    user=models.ForeignKey(to=User,verbose_name="게시인",on_delete=models.CASCADE)
    product_name=models.CharField("상품이름",unique=True,max_length=100,error_messages={'unique':'이미 존재하는 상품명입니다.'})
    product_img=models.ImageField("상품이미지",upload_to='images/product/')
    category=models.ManyToManyField(to=Category,verbose_name="카테고리")
    price=models.IntegerField("가격")
    uploaded_at=models.DateField("상품업로드날짜",auto_now_add=True)
    started_at = models.DateField("노출시작일")
    ended_at = models.DateField("노출종료일")

    def __str__(self):
        return self.product_name

