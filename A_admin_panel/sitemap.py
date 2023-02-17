from django.contrib.sitemaps import Sitemap
from A_admin_panel.models import *

class ItemSiteMap(Sitemap):
    def items(self):
        return SEOMap.objects.all()