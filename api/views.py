from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from myuser.models import MyUser
from .serializers import MyUserSerializer
from homeowner.models import Homeowner
from .serializers import HomeownerSerializer
from supplier.models import Supplier
from .serializers import SupplierSerializer
from material.models import Material
from .serializers import MaterialSerializer
from brand.models import Brand
from .serializers import BrandSerializer

# Create your views here.

class MyUserListView(APIView):
    def get(self, request):
        myusers = MyUser.objects.all()
        serializer = MyUserSerializer(myusers, many = True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = MyUserSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class MyUserDetailView(APIView):
    def get(self, request, id):
        myuser = MyUser.objects.get(id = id)
        serializer = MyUserSerializer(myuser)
        return Response(serializer.data)
    

def put(self, request, id):
        student = MyUser.objects.get(id = id)
        serializer = MyUserSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)



class HomeownerListView(APIView):
    def get(self, request):
        homeowners = Homeowner.objects.all()
        serializer = HomeownerSerializer(homeowners, many = True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = HomeownerSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class HomeownerDetailView(APIView):
    def get(self, request, id):
        homeowner = Homeowner.objects.get(id = id)
        serializer = HomeownerSerializer(homeowner)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = Homeowner.objects.get(id = id)
        serializer = HomeownerSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
    

    
class SupplierListView(APIView):
    def get(self, request):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many = True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = SupplierSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class SupplierDetailView(APIView):
    def get(self, request, id):
        supplier = Supplier.objects.get(id = id)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = Supplier.objects.get(id = id)
        serializer = SupplierSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)


class MaterialListView(APIView):
    def get(self, request):
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many = True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = MaterialSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class MaterialDetailView(APIView):
    def get(self, request, id):
        material = Material.objects.get(id = id)
        serializer = MaterialSerializer(material)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = Material.objects.get(id = id)
        serializer = MaterialSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
    


class BrandListView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many = True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = BrandSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class BrandDetailView(APIView):
    def get(self, request, id):
        brand = Brand.objects.get(id = id)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = Brand.objects.get(id = id)
        serializer = BrandSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        



        