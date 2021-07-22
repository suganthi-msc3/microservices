from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Product,User
from .serializer import ProductSerializer,UserSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from django.core import serializers
import random,json
from json import dumps,loads
from .producer import publish

from django.shortcuts import render

# Create your views here.
class ProductViewset(viewsets.ViewSet):
    def list(self,request):
        products= Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        # publish('Product_list',serializer.data)
        return Response(serializer.data)
    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created',serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def update(self,request,pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated',serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    def destroy(self,request,pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted',pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self,_):
        product = User.objects.all()
        serializer = UserSerializer(instance=product, many=True)
        users=serializer.data
        user=random.choice(users)
        print(user)
        return Response(user,status=status.HTTP_202_ACCEPTED)



