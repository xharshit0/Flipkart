from rest_framework import serializers
from customer.models import *

class GetCustomerserializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = "__all__"

class GetAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAddress
        fields = "__all__"

class GetCustomerDetailsAddressSerializer(serializers.ModelSerializer):
    customer_address = GetAddressSerializer(many = True)

    class Meta:
        model = Customers
        fields = ('first_name','last_name','mobile','address','age','country','city')