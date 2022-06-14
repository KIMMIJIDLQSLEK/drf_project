from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField("카테고리 이름",primary_key=True, max_length=100)
    introduction=models.TextField("설명")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Categories'
