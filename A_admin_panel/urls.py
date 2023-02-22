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
    path('create_product_admin/',CreateProductAdmin.as_view(),name='create_product_admin'),
    path('update_product_admin/<int:pk>/',UpdateProductAdmin.as_view(),name='update_product_admin'),
    path('delete_product_admin/<int:pk>/',DeleteProductAdmin.as_view(),name='delete_product_admin'),
    path('info_product_admin/<int:pk>/',info_product_admin,name='info_product_admin'),
    # Advantags CRUD
    path('all_advantags_admin/',AllAdvantagsAdmin.as_view(),name='all_advantags_admin'),
    path('create_advantags_admin/',CreateAdvantagsAdmin.as_view(),name='create_advantags_admin'),
    path('update_advantags_admin<int:pk>/',UpdateAdvantagsAdmin.as_view(),name='update_advantags_admin'),
    path('delete_advantags_admin/<int:pk>/',DeleteAdvantagsAdmin.as_view(),name='delete_advantags_admin'),

    # Brands CRUD
    path('all_brands_admin/',AllBrandsAdmin.as_view(),name='all_brands_admin'),
    path('create_brands_admin/',CreateBrandsAdmin.as_view(),name='create_brands_admin'),
    path('update_brands_admin<int:pk>/',UpdateBrandssAdmin.as_view(),name='update_brands_admin'),
    path('delete_brands_admin/<int:pk>/',DeleteABrandsAdmin.as_view(),name='delete_brands_admin'),

    path('orders/',orders,name='orders'),
    path('create_prodcut_with_excel/',create_prodcut_with_excel,name='create_prodcut_with_excel'),

    # Pochta CRUD
    path('all_pochta_admin/',AllPochtaAdmin.as_view(),name='all_pochta_admin'),
    path('create_pochta_admin/',CreatePochtaAdmin.as_view(),name='create_pochta_admin'),
    path('update_pochta_admin<int:pk>/',UpdatePochtaAdmin.as_view(),name='update_pochta_admin'),
    path('delete_pochta_admin/<int:pk>/',DeletePochtaAdmin.as_view(),name='delete_pochta_admin'),

    path('RandUpdate/',RandUpdate.as_view()),

    # seo urls
    path('all_seo_admin/',AllSEOAdmin.as_view(),name='all_seo_admin'),
    path('create_seo_admin/',CreateSEOAdmin.as_view(),name='create_seo_admin'),
    path('update_seo_admin/<int:pk>/',UpdateSEOAdmin.as_view(),name='update_seo_admin'),
]
