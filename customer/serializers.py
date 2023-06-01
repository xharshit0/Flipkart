from rest_framework import serializer
from rest_framework import *

class GetCustomerSerializer(serializers.ModelSerializer):

    class Meta:
    model = Customer
    fields ="__all__"


    class CustomerAddressSerializer(serializer.ModelSerializer):
    class Meta:
    models = CustomerAddress
    fields = "__all__"


    class CustomerDetailAddressSerializer(serializer.ModelSerializer)
    Customer_addresses
    class Meta:
    models = Customer
    fields ='first_name' 'last_name'
   
