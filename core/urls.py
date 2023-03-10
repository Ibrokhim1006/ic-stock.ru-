from django.contrib import admin
from django.urls import path,include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap




urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin_panel/',include('A_admin_panel.urls')),
    path('',include('B_sayt.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]
