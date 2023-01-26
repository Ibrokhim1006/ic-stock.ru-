from django.db import models

class Advantages(models.Model):
    title = models.CharField(max_length=250,verbose_name="Преимущества")
    img = models.FileField(upload_to="Advantages/")

    def __str__(self):
        return self.title

class Brand(models.Model):
    name = models.CharField(max_length=250,verbose_name="Имя бренда")
    img_brend = models.ImageField(upload_to='brend/',verbose_name="Фирменное изображение")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Categoriya(models.Model):
    name = models.CharField(max_length=250,verbose_name="Название категории")
    img_categoriya = models.ImageField(upload_to="catgeoriya/",null=True,blank=True,verbose_name="Изображение категории")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name