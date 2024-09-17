from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=255,verbose_name='Название категории:',unique=True)
    category_slug = models.SlugField(verbose_name='Слаг категорий',max_length=255,unique=True)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'

    def __str__(self):
        return self.category_name

class Brands(models.Model):
    brand_name = models.CharField(max_length=255,verbose_name='производитель:')
    brand_slug = models.SlugField(max_length=255,verbose_name='слаг:')
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.brand_name
    

class Product(models.Model):
    name = models.CharField(max_length=250,verbose_name='Название:')
    price = models.IntegerField(verbose_name='Цена:')
    img1 = models.ImageField(verbose_name='картинка1:',upload_to='media')
    img2 = models.ImageField(verbose_name='картинка2:',upload_to='media',blank=True,null=True)
    img3 = models.ImageField(verbose_name='картинка3:',upload_to='media',blank=True,null=True)
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(verbose_name='описание:')
    characteristics = models.TextField(verbose_name='характеристики:')
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

class Comments(models.Model):
    text = models.TextField(verbose_name='Комментарий:')
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True,verbose_name='Дата добавления:')
    class Meta:
        verbose_name = 'Комментария'
        verbose_name_plural = 'Комментарий'

    def __str__(self):
        return self.text
 
