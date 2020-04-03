from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=32)
    weight= models.FloatField()
    price=models.FloatField()
    created_date = models.DateField()
    updated_date = models.DateField()