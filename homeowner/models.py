from django.db import models
from myuser.models import MyUser

# # Create your models here.


class Homeowner(models.Model):
    homeowner_id = models.AutoField(primary_key=True)
    myuser = models.ForeignKey(MyUser, related_name='homeowners', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.homeowner_id} {self.address}"