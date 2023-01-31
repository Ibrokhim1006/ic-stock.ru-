from django import forms 
from A_admin_panel.models import *

class CategoryForms(forms.ModelForm):
    class Meta:
        model = Categoriya
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'img_categoriya': forms.FileInput(attrs={'class':'form-control'})
        }
        labels = {
            'name': 'Имя каталога',
            'img_categoriya': 'Икона'
        }

class ProductsForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','manufacturer','categorsiya_id','price','amunt','img','description',]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'manufacturer': forms.TextInput(attrs={'class':'form-control'}),
            'categorsiya_id': forms.Select(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'amunt': forms.TextInput(attrs={'class':'form-control'}),
            'img': forms.FileInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'})
        }
        labels = {
            'name': 'Наименование',
            'manufacturer': 'Производитель',
            'categorsiya_id': 'Каталог товаров',
            'price': 'Стоимость',
            'amunt': 'Доступное количество (не менее)',
            'img': 'Изображение продукта',
            'description': 'Описание'
        }

class AdvantagsForms(forms.ModelForm):
    class Meta:
        model = Advantages
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'img': forms.FileInput(attrs={'class':'form-control'})
        }

        labels = {
            'title': 'Преимущества',
            'img': 'Значок преимущества'
        }

class BrandForms(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'urls': forms.URLInput(attrs={'class':'form-control'}),
            'img_brend': forms.FileInput(attrs={'class':'form-control'})
        }

        labels = {
            'name': 'Имя бренда',
            'urls': 'Сайт бренда',
            'img_brend': 'Фирменное изображение'
        }