from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth .decorators import login_required
from django.views.generic.edit import UpdateView,CreateView
from django.views.generic import ListView,DeleteView,DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy,reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponseRedirect
import random
import pandas as pd
from django.core.files.storage import FileSystemStorage
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
    return redirect('/')

   

@login_required
def home_admin(request):
    return render(request,'admin_panel/index.html')

@login_required
def all_category_admin(request):
    context = {}
    context['objects_list'] = Categoriya.objects.all()
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
    context['objects_list'].reverse()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(context['objects_list'], 120) # 6 employees per page
    try:
        context['page_obj'] = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        context['page_obj'] = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        context['page_obj'] = paginator.page(paginator.num_pages)
    
    return render(request,'admin_panel/product/all_product.html',context)
@login_required
def create_product_admin(request):
    context ={}
    form = ProductsForms(request.POST or None)
    if form.is_valid():
        radd = str(random.randint(100000000,999999999))
        
        form.save()
        return redirect('all_product_admin')
    context['form']= form
    return render(request,'admin_panel/product/create.html',context)

class CreateProductAdmin(CreateView):
    model = Product
    form_class = ProductsForms
    template_name = 'admin_panel/product/create.html'
    success_url = reverse_lazy('all_product_admin')

# class UpdateProductAdmin(UpdateView):
#     model = Product
#     form_class = ProductsForms
#     template_name = 'admin_panel/product/update.html'
#     success_url = reverse_lazy('all_product_admin')
@login_required
def update_product_admin(request,pk):
    context ={}
    obj = get_object_or_404(Product, id = pk)
    form = ProductsForms(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('all_product_admin')

    context["form"] = form
    return render(request,'admin_panel/product/all_product.html',context)
class RandUpdate(APIView):
    def get(self,request,format=None):
        radd = str(random.randint(100000000,999999999))
        pr = Product.objects.all().update(amunt=radd)
        return Response({'msg':'ok'})
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


@login_required
def orders(request):
    context = {}
    context['objects_list'] = ClientPost.objects.all().order_by('-id')
    return render(request,'admin_panel/orders.html',context)

@login_required
def create_prodcut_with_excel(request):
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)              
        empexceldata = pd.read_excel(filename)        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            print(dbframe)
    return render(request,'admin_panel/create.html')


# Pochta CRUD
class AllPochtaAdmin(ListView):
    model = Delivery
    template_name = 'admin_panel/pochta/all_list.html'
class CreatePochtaAdmin(CreateView):
    model = Delivery
    form_class = PochtaForms
    template_name = 'admin_panel/pochta/create.html'
    success_url = reverse_lazy('all_pochta_admin')
class UpdatePochtaAdmin(UpdateView):
    model = Delivery
    form_class = PochtaForms
    template_name = 'admin_panel/pochta/update.html'
    success_url = reverse_lazy('all_pochta_admin')
class DeletePochtaAdmin(DeleteView):
    model = Delivery
    template_name = 'admin_panel/pochta/delete.html'
    success_url = reverse_lazy('all_pochta_admin')


# SEO optimization
class AllSEOAdmin(ListView):
    model = SeoContent
    template_name = 'admin_panel/seo/all_objects.html'
class CreateSEOAdmin(CreateView):
    model = SeoContent
    form_class = SeoForms
    template_name = 'admin_panel/seo/create.html'
    success_url = reverse_lazy('all_seo_admin')
class UpdateSEOAdmin(UpdateView):
    model = SeoContent
    form_class = SeoForms
    template_name = 'admin_panel/seo/update.html'
    success_url = reverse_lazy('all_seo_admin')