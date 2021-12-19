from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import CharField

class Materials(models.Model):
    material_name = models.CharField(max_length=30)
    price = models.FloatField()
    
    def check_price(self):
        return self.price
    
    def __str__(self):
        return self.material_name
