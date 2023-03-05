from django.urls import path
from B_sayt.views import *

urlpatterns = [
    path('',index,name='index'),
    path('delivery/',delivery,name='delivery'),
    path('contact/',contact,name='contact'),
    path('all_category/',all_category,name='all_category'),
    path('<str:urls>/',in_categor_product,name='in_categor_product'),
    path('<str:atrikul>',in_product,name='in_product'),
    path('all_product_search_view/',AllProductSearchView.as_view()),
    path('client_post/<int:id>/',client_post,name='client_post'),

    path('supply_line/',supply_line,name='supply_line'),
    path('quality/',quality,name='quality'),
    # path('DeleteProductView/',DeleteProductView.as_view())

    # path('create_product_view/<str:atrikul>/',CreateProductView.as_view,name='create_product_view')
]