from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    created_date = models.DateField()
    updated_date = models.DateField()