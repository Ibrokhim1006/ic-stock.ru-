from django.contrib.auth.models import User,Group
from rest_framework import serializers
from A_admin_panel.models import *


class AllSearchCtaegor(serializers.ModelSerializer):
    class Meta:
        model = Categoriya
        fields = '__all__'

class AllSearchProduct(serializers.ModelSerializer):
    categorsiya_id = AllSearchCtaegor(read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','atrikul','categorsiya_id',]