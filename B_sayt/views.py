from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse , HttpResponseRedirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from django.db.models import Q
from B_sayt.serializers import *
from A_admin_panel.models import *



def index(request):
    context = {}
    context['objects_advend'] = Advantages.objects.all()
    context['objects_brend'] = Brand.objects.all()[:7]
    context['objects_product'] = Product.objects.all().order_by('-id')[:6]
    if request.method=='POST':
        full_name = request.POST.get('full_name')
        company = request.POST.get('company')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        if full_name=='' or company=='' or email=='' or phone=='' or content=='':
            context['error'] = "Заполните информацию !"
            return render(request,'sayt/index.html',context)
        supply_lines = SupplyLine(full_name=full_name,company=company,email=email,phone=phone,content=content)
        supply_lines.save()
        return redirect('index') 
    return render(request,'sayt/index.html',context)

def delivery(request):
    context = {}
    context['objects_all'] = Delivery.objects.all()
    return render(request,'sayt/delivery.html',context)

def contact(request):
    context = {}
    if request.method=='POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        predmets = request.POST.get('predmets')
        content = request.POST.get('content')
        if full_name=='' or email=='' or predmets=='' or content=='':
            context['error'] = "Заполните информацию !"
            return render(request,'sayt/contact.html',context)
        con = Contact(full_name=full_name,email=email,predmets=predmets,content=content)
        con.save()
        return redirect('contact')
    return render(request,'sayt/contact.html',context)

def all_category(request):
    context = {}
    context['objects_brend'] = Brand.objects.all()
    context['objects_all'] = Categoriya.objects.all()
    return render(request,'sayt/all_category.html',context)

def in_categor_product(request,urls):
    context = {}
    context['categor'] = Categoriya.objects.get(urls=urls)
    context['objects_product'] = Product.objects.filter(categorsiya_id=context['categor'].id).order_by('-id')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(context['objects_product'], 30) # 6 employees per page


    try:
        context['page_obj'] = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        context['page_obj'] = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        context['page_obj'] = paginator.page(paginator.num_pages)

    return render(request,'sayt/in_categor_product.html',context)

def in_product(request,brend_id__ur,atrikul):
    context = {}
    context['objects'] = Product.objects.get(brend_id__ur=brend_id__ur,atrikul=atrikul)
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
    filter_backends = [filters.SearchFilter]
    search_fields = ['atrikul','name',]

def saearch_product(request):
    if request.method=='GET':
        atrikul = request.GET.get('atrikul')
        name =  request.GET.get('name')
    
    a = Product.objects.filter(atrikul=atrikul).values()
    return JsonResponse({'data':list(a)})

# {
#     'name': 'Configuration',
#     'data':'Single'
# },



def supply_line(request):
    context = {}
    context['objects_brend'] = Brand.objects.all()
    if request.method=='POST':
        full_name = request.POST.get('full_name')
        company = request.POST.get('company')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        if full_name=='' or company=='' or email=='' or phone=='' or content=='':
            context['error'] = "Заполните информацию !"
            return render(request,'sayt/supply_line.html',context)
        supply_lines = SupplyLine(full_name=full_name,company=company,email=email,phone=phone,content=content)
        supply_lines.save()
        return redirect('supply_line')
    return render(request,'sayt/supply_line.html',context)

def quality(request):
    context = {}
    if request.method=='POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        if full_name=='' or phone=='':
            context['error'] = "Заполните информацию !"
            return render(request,'sayt/index.html',context)
        ques = Questions(full_name=full_name,phone=phone)
        ques.save()
        return redirect('quality')
    return render(request,'sayt/quality.html',context)


class CreateProductView(APIView):
    def post(self,request,atrikul):
        objects = Product.objects.filter(atrikul=atrikul)[0]
        name = request.data['name']
        objects.name=name
        objects.save()

        return Response({'data':'succsess'})

class DeleteProductView(APIView):
    def get(self,request):
        objects = Product.objects.all()
        objects.delete()
        return Response({'data':'succsess'})


def create_product_view(request,atrikul):
    objects = Product.objects.filter(atrikul=atrikul)
    if request.method=='POST':
        name = request.POST.get('name')
        img_url =  request.POST.get('img_url')
        table =  request.POST.get('table')
        description =  request.POST.get('description')
        if name=='':
            return JsonResponse({'data':'error'})
    objects.name=name
    objects.img_url=img_url
    objects.table=table
    objects.description=description
    objects.save()
    return JsonResponse({'data':'succsess'})