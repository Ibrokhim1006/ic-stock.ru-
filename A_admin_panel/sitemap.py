from django.contrib.sitemaps import Sitemap
from A_admin_panel.models import *



class PostSitemap(Sitemap):


    def items(self):
        return Product.objects.all()

