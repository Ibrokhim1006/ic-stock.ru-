from django.urls import path
from B_sayt.views import *

urlpatterns = [
    path('index/',index,name='index'),
    path('delivery/',delivery,name='delivery'),
    path('contact/',contact,name='contact'),
    path('all_category/',all_category,name='all_category'),
    path('in_categor_product/<int:id>/',in_categor_product,name='in_categor_product'),
    path('in_product/<int:id>/',in_product,name='in_product'),
    path('all_product_search_view/',saearch_product),
    path('client_post/<int:id>/',client_post,name='client_post'),
    path('',get_client_ip,name='get_client_ip'),

    path('supply_line/',supply_line,name='supply_line'),
    path('quality/',quality,name='quality')
]