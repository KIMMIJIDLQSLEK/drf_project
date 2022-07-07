# Generated by Django 4.0.5 on 2022-07-06 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(error_messages={'unique': '이미 존재하는 상품명입니다.'}, max_length=100, unique=True, verbose_name='상품이름'),
        ),
    ]