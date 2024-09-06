from django.db import models
# from homeowner.models import Homeowner
# from supplier.models import Supplier

# Create your models here.

class MyUser(models.Model):
    user_id = models.AutoField(primary_key= True)
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200)
    email = models.EmailField()
    password = models.CharField(max_length= 200)
    user_role = models.CharField(max_length= 200)
    phone_number = models.CharField(max_length= 200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"