from django.urls import path
from B_sayt.views import *

urlpatterns = [
    path('',index,name='index'),
]