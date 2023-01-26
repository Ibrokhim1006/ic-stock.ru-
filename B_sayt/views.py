from django.shortcuts import render
from A_admin_panel.models import *

def index(request):
    context = {}
    context['objects_advend'] = Advantages.objects.all()
    context['objects_brend'] = Brand.objects.all()
    return render(request,'sayt/index.html',context)

def delivery(request):

    return render(request,'sayt/delivery.html')

def contact(request):
    return render(request,'sayt/contact.html')