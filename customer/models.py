 from django.db import models

# Create your models here.

class Customers(models.Model):
     
     first_name = models.CharField(max_length=15,null=True,blank=True)
     last_name = models.CharField(max_length=15,null=True,blank=True)
     mobile = models.IntegerField(null=True,blank=True)
     address = models.TextField(null=True,blank=True)
     age = models.IntegerField(null=True,blank=True)
     country = models.CharField(max_length=15,null=True,blank=True)
     city = models.CharField(max_length=15,null=True,blank=True)
     dob = models.DateField(max_length=15,null=True,blank=True)
     order = models.TextField(null=True,blank=True)

     def __str__(self):
     return self.first_name

class CustomerAddress(models.Model):
     customer = models.ForeignKey(Customers,on_delete=models.CASCADE,null=True,related_name='customer_address')
     street_name = models.CharField(max_length=30,null=True,blank=True)
     street_number = models.IntegerField(null=True,blank=True)
     city = models.CharField(max_length=30,null=True,blank=True)
     state = models.CharField(max_length=30,null=True,blank=True)
     country = models.CharField(max_length=30,null=True,blank=True)
     pincode = models.IntegerField(null=True,blank=True)

     def __str__(self):
     return self.street_name

class CustomerAdhaar(models.Model):
     customer = models.OneToOneField(Customers,on_delete=models.CASCADE)
     adhaar_number = models.IntegerField(null=True,blank=True)
     adhaar_name = models.CharField(max_length=35, null=True, blank=True)

     def __str__(self):
     return self.adhaar_name
