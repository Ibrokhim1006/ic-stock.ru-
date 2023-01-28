from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth .decorators import login_required
from django.views.generic.edit import UpdateView,CreateView
from django.views.generic import ListView,DeleteView,DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
import random
from A_admin_panel.models import *
from A_admin_panel.forms import *

def login_admin(request):
    context = {}
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username=='' or password=='':
            context['error'] = "Вы не ввели логин или пароль !"
            return render(request,'auht/sigin_in.html',context)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('all_category_admin')
        else:
            context['error'] = "Неверный логин или пароль !"
    return render(request,'auht/sigin_in.html',context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('login_admin')

@login_required
def home_admin(request):
    return render(request,'admin_panel/index.html')

@login_required
def all_category_admin(request):
    context = {}
    context['objects_list'] = Categoriya.objects.all().order_by('-id')
    return render(request,'admin_panel/category/all_category.html',context)

# Categoriya CRUD
class CreateCategoryAdmin(CreateView):
    model = Categoriya
    form_class = CategoryForms
    template_name = 'admin_panel/category/create.html'
    success_url = reverse_lazy('all_category_admin')
class UpdateCategoryAdmin(UpdateView):
    model = Categoriya
    form_class = CategoryForms
    template_name = 'admin_panel/category/update.html'
    success_url = reverse_lazy('all_category_admin')
class DeleteCategoryAdmin(DeleteView):
    model = Categoriya
    template_name = 'admin_panel/category/delete.html'
    success_url = reverse_lazy('all_category_admin')

# PRODUCT CRUD
@login_required
def all_product_admin(request):
    context = {}
    context['objects_list'] = Product.objects.all().order_by('-id')
    return render(request,'admin_panel/product/all_product.html',context)
@login_required
def create_product_admin(request):
    context = {}
    context['object_list'] = Categoriya.objects.all()
    if request.method=='POST':
        name = request.POST.get('name')
        manufacter = request.POST.get('manufacter')
        categorsiya_id = request.POST.get('categorsiya_id')
        try:
            get_catgeor = Categoriya.objects.get(id=categorsiya_id)
        except Categoriya.DoesNotExist:
            get_catgeor=  None
        price = request.POST.get('price')
        amunt = request.POST.get('amunt')
        img = request.FILES.get('img')
        description = request.POST.get('description')
        if name=='' or manufacter=='' or categorsiya_id=='' or price=='' or amunt=='' or img=='' or description=='':
            context['error'] = "Заполните информацию !"
            return render(request,'admin_panel/product/create.html',context)
        genret_artikul = random.randint(100000000,999999999)
        product_save = Product(name=name,img=img,price=price,categorsiya_id=get_catgeor,atrikul=genret_artikul,manufacturer=manufacter,description=description,amunt=amunt)
        product_save.save()
        return redirect('all_product_admin')
    return render(request,'admin_panel/product/create.html',context)
class UpdateProductAdmin(UpdateView):
    model = Product
    form_class = ProductsForms
    template_name = 'admin_panel/product/update.html'
    success_url = reverse_lazy('all_product_admin')
class DeleteProductAdmin(DeleteView):
    model = Product
    template_name = 'admin_panel/product/delete.html'
    success_url = reverse_lazy('all_product_admin')
@login_required
def info_product_admin(request,pk):
    context = {}
    context['objects'] = Product.objects.get(id=pk)
    return render(request,'admin_panel/product/info.html',context)

# Advantags CRUD
class AllAdvantagsAdmin(ListView):
    model = Advantages
    template_name = 'admin_panel/advantages/all_list.html'
class CreateAdvantagsAdmin(CreateView):
    model = Advantages
    form_class = AdvantagsForms
    template_name = 'admin_panel/advantages/create.html'
    success_url = reverse_lazy('all_advantags_admin')
class UpdateAdvantagsAdmin(UpdateView):
    model = Advantages
    form_class = AdvantagsForms
    template_name = 'admin_panel/advantages/update.html'
    success_url = reverse_lazy('all_advantags_admin')
class DeleteAdvantagsAdmin(DeleteView):
    model = Advantages
    template_name = 'admin_panel/advantages/delete.html'
    success_url = reverse_lazy('all_advantags_admin')

# Brand CRUD
class AllBrandsAdmin(ListView):
    model = Brand
    template_name = 'admin_panel/brand/all_list.html'
class CreateBrandsAdmin(CreateView):
    model = Brand
    form_class = BrandForms
    template_name = 'admin_panel/brand/create.html'
    success_url = reverse_lazy('all_brands_admin')
class UpdateBrandssAdmin(UpdateView):
    model = Brand
    form_class = BrandForms
    template_name = 'admin_panel/brand/update.html'
    success_url = reverse_lazy('all_brands_admin')
class DeleteABrandsAdmin(DeleteView):
    model = Brand
    template_name = 'admin_panel/brand/delete.html'
    success_url = reverse_lazy('all_brands_admin')