from django.db import models

# Create your models here.
 
class Customer_Address(models.Model):
     first_name = models.CharField(max_length=15,null=True,Blank=True)
     last_name = models.CharField(max_length=15,null=True,Blank=True)
     mobile = models.IntegerField(null=True,Blank=True)
     address = models.TextField(null=True,Blank=True)
     age = models.IntegerField(null=True,Blank=True)
     country = models.CharField(max_length=20,null=True,Blank=True)
     city = models.CharField(max_length=20,null=True,Blank=True)
     dob = models.DateField(max_length=20,null=True,Blank=True)
 
     def __str__(self):
      return self.first_name