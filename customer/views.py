from django.shortcuts import render
from customer.models import *
from customer.serializers import *

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class GetCustomerView(APIView):

    def get(self,request):
        instance = Customers.objects.all()
        serializer = GetCustomerserializer(instance,many=True)
        return Response(serializer.data)

    def post(self,request):
        params = request.data
        print("Data",params)
        serializer = GetCustomerserializer(data=params)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Successfully sent")

class GetAddressView(APIView):

    def get(self,request):
        instance = CustomerAddress.objects.all()
        serializers = GetAddressSerializer(instance,many= True)
        return Response(serializers.data)

class GetCustomerDetailsAddressView(APIView):

    def get(self,request,pk):
        instance = Customers.objects.filter(id = pk)
        serializers = GetCustomerDetailsAddressSerializer(instance,many = True)
        return Response(serializers.data)