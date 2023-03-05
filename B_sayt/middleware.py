from django.shortcuts import redirect, render
from A_admin_panel.models import *

def all_ceo(get_res):
    def middleware(request):
        request.get_seo = SeoContent.objects.all()
        response = get_res(request)
        # request.get_description = SeoContent.objects.all()
        # response = get_res(request)
        return response
    return middleware
