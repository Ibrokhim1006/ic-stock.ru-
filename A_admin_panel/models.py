from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
import random

# random_string = str(random.randint(100000000, 999999999))

class Advantages(models.Model):
    title = models.CharField(max_length=250,verbose_name="Преимущества")
    img = models.FileField(upload_to="Advantages/")

    def __str__(self):
        return self.title

class Brand(models.Model):
    name = models.CharField(max_length=250,verbose_name="Имя бренда")
    img_brend = models.FileField(upload_to='brend/',verbose_name="Фирменное изображение")
    ur = models.CharField(max_length=20,null=True,blank=True)
    urls = models.URLField(null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Categoriya(models.Model):
    name = models.CharField(max_length=250,verbose_name="Название категории")
    urls = models.CharField(max_length=250,null=True,blank=True)
    decription = models.TextField(null=True,blank=True)
    img_categoriya = models.FileField(upload_to="catgeoriya/",null=True,blank=True,verbose_name="Изображение категории")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250,null=True,blank=True)
    img = models.FileField(upload_to="product/",null=True,blank=True)
    price = models.CharField(max_length=250,null=True,blank=True)
    categorsiya_id = models.ForeignKey(Categoriya,on_delete=models.CASCADE,null=True,blank=True)
    brend_id = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    atrikul = models.CharField(max_length=250,null=True,blank=True)    
    manufacturer = models.CharField(max_length=250,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    amunt = models.CharField(max_length=250,null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

class ClientPost(models.Model):
    full_name = models.CharField(max_length=250)
    pochta = models.EmailField()
    phone = models.CharField(max_length=250)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class SupplyLine(models.Model):
    full_name = models.CharField(max_length=250,null=True,blank=True)
    company = models.CharField(max_length=250,null=True,blank=True)
    email = models.CharField(max_length=250,null=True,blank=True)
    phone = models.CharField(max_length=250,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    predmets = models.CharField(max_length=250)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Questions(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name

class Delivery(models.Model):
    name = models.CharField(max_length=250)
    img = models.FileField(upload_to='delivery/')

    def __str__(self):
        return self.name





class SeoCategory(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class SeoContent(models.Model):
    title = models.CharField(max_length=250,null=True,blank=True)
    id_seo_catgeory = models.ForeignKey(SeoCategory,on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Zayafka(models.Model):
    fullName = models.CharField(max_length=250,null=True,blank=True)
    e_mail = models.CharField(max_length=250,null=True,blank=True)
    e_phone = models.CharField(max_length=250,null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullName
    

class Search_Request(models.Model):
    name = models.CharField(max_length=250)
    num = models.SmallIntegerField(null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name