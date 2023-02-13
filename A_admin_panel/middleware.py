from django.shortcuts import redirect, render
from A_admin_panel.models import *

def all_categoriya(get_res):
    def middleware(request):
        request.get_catgor =Categoriya.objects.all().order_by('-id')
        response = get_res(request)

        return response
    return middleware