from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import *
from customer.serializers import *

# Create your views here.
class GetCustomerView(APIview):

    def get(self,request):
        instance = Customer,object.all()
        serializer =GetcustomerSerializer(instance,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        params = request.data
        print("Data",params)
        serializers =GetcustomerSerializer(data = params)
        serializers.valid(FalseException=True )
        serializers.save()
        return Response({"message","Save Successfully"}) 

class CustomerAddressViews(APIView):

  def get(self,request):
       instance=customer.object.all()
       serializer=  CustomerAddressSerializer(instance,many=True)            
       return Response(serializer.data)         

      class CustomerDetailAddressView(APIView):
        def get(self,request,pk):
            instance =customer.object.filter(id=pk)     
            serializer = CustomerDetailAddressSerializer(instance,many = True)                                                                                                