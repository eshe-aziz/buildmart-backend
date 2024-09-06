from django.db import models
from material.models import Material

# Create your models here.

class Brand(models.Model):
    brand_id = models.AutoField(primary_key= True)
    material_id = models.ForeignKey(Material, related_name='brands', on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.brand_id} {self.brand_name}"