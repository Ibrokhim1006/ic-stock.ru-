from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin,ImportExportModelAdmin

from A_admin_panel.models import *

admin.site.register(Advantages)
admin.site.register(Brand)

class CategorEx(ImportExportModelAdmin):
    pass
admin.site.register(Categoriya, CategorEx)
class ProductEx(ImportExportModelAdmin):
    pass
admin.site.register(Product, ProductEx)
admin.site.register(ClientPost)