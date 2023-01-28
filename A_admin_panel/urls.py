from django.urls import path
from A_admin_panel.views import *

urlpatterns = [
    path('',login_admin,name='login_admin'),
    path('logout_user/',logout_user,name='logout_user'),
    path('home_admin/',home_admin,name='home_admin'),
    # CATEGORIYA CRUD
    path('all_category_admin/',all_category_admin,name='all_category_admin'),
    path('create_category_admin/',CreateCategoryAdmin.as_view(),name='create_category_admin'),
    path('update_category_admin/<int:pk>/',UpdateCategoryAdmin.as_view(),name='update_category_admin'),
    path('delete_category_admin/<int:pk>/',DeleteCategoryAdmin.as_view(),name='delete_category_admin'),
    # PRODCUT CRUD
    path('all_product_admin/',all_product_admin,name='all_product_admin'),
    path('create_product_admin/',create_product_admin,name='create_product_admin'),
    path('update_product_admin/<int:pk>/',UpdateProductAdmin.as_view(),name='update_product_admin'),
    path('delete_product_admin/<int:pk>/',DeleteProductAdmin.as_view(),name='delete_product_admin'),
    path('info_product_admin/<int:pk>/',info_product_admin,name='info_product_admin')

]
