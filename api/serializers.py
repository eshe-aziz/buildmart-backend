from rest_framework import serializers
from myuser.models import MyUser
from homeowner.models import Homeowner
from supplier.models import Supplier
from material.models import Material
from brand.models import Brand

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

class HomeownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeowner
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'