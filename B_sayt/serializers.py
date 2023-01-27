from django.contrib.auth.models import User,Group
from rest_framework import serializers
from A_admin_panel.models import *

class AllSearchProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'