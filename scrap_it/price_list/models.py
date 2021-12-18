from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import CharField

class Materials(models.Model):
    material_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2)
