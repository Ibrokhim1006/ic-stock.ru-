from django.urls import path
from B_sayt.views import *

urlpatterns = [
    path('',index,name='index'),
    path('delivery/',delivery,name='delivery'),
    path('contact/',contact,name='contact'),
]