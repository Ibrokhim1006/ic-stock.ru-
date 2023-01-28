from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from B_sayt.serializers import *
from A_admin_panel.models import *

def index(request):
    context = {}
    context['objects_advend'] = Advantages.objects.all()
    context['objects_brend'] = Brand.objects.all()
    context['objects_product'] = Product.objects.all().order_by('-id')[:6]
    if request.method=='POST':
        search = request.POST.get('search')
        context['reault_search'] = Product.objects.filter(name=search)
        
    return render(request,'sayt/index.html',context)

def delivery(request):

    return render(request,'sayt/delivery.html')

def contact(request):
    return render(request,'sayt/contact.html')

def all_category(request):
    context = {}
    context['objects_brend'] = Brand.objects.all()
    context['objects_all'] = Categoriya.objects.all()
    return render(request,'sayt/all_category.html',context)

def in_categor_product(request,id):
    context = {}
    context['categor'] = Categoriya.objects.get(id=id)
    context['objects_product'] = Product.objects.filter(categorsiya_id=id).order_by('-id')
    return render(request,'sayt/in_categor_product.html',context)

def in_product(request,id):
    context = {}
    context['objects'] = Product.objects.get(id=id)
    return render(request,'sayt/in_product.html',context)

def client_post(request,id):
    context = {}
    context['object'] = Product.objects.get(id=id)
    if request.method=="POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if full_name=='' or email=='' or phone=='':
            context['error'] = "Заполните информацию !"
            return render(request,'sayt/client_post.html',context)
        post_client = ClientPost(full_name=full_name,pochta=email,phone=phone,product_id=context['object'])
        post_client.save()
        context['error'] = "s"
        return render(request,'sayt/client_post.html',context)
    return render(request,'sayt/client_post.html',context)

class AllProductSearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = AllSearchProduct
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'