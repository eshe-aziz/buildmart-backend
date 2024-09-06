from django.db import models
from homeowner.models import Homeowner
from myuser.models import MyUser

# Create your models here.

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key= True)
    myuser = models.ForeignKey(MyUser, related_name='suppliers', on_delete=models.CASCADE)
    company_name = models.CharField(max_length= 200)
    location = models.CharField(max_length= 200)
    homeowner = models.ForeignKey('homeowner.Homeowner', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.company_name} {self.location}"