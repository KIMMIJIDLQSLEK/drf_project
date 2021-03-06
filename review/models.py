from django.db import models
from user.models import User
from product.models import Product

# Create your models here.
class Review(models.Model):
    author=models.ForeignKey(to=User,verbose_name="게시물작성자",on_delete=models.CASCADE) #user와 일대다관계
    product=models.ForeignKey(to=Product,verbose_name="상품",on_delete=models.CASCADE)
    grade=models.IntegerField("평점")
    contents=models.TextField("리뷰내용")
    created_at=models.DateField("리뷰작성날짜",auto_now_add=True)
    update_check=models.BooleanField("리뷰수정여부",default=False)

    def __str__(self):
        return self.contents