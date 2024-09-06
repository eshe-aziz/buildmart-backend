from django.db import models

# Create your models here.

class Material(models.Model):
    material_id = models.AutoField(primary_key= True)
    material_name = models.CharField(max_length= 50)
    description = models.CharField(max_length= 200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image= models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.material_name} {self.description}"