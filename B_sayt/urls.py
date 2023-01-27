from django.urls import path
from B_sayt.views import *

urlpatterns = [
    path('',index,name='index'),
    path('delivery/',delivery,name='delivery'),
    path('contact/',contact,name='contact'),
    path('all_category/',all_category,name='all_category'),
    path('in_categor_product/<int:id>/',in_categor_product,name='in_categor_product'),
    path('in_product/<int:id>/',in_product,name='in_product'),
    path('all_product_search_view/',AllProductSearchView.as_view()),
]