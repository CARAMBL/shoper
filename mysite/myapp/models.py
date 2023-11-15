from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class Product (models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    name = models.CharField (max_length=100)
    price = models.IntegerField()
    disc = models.CharField (max_length=500, null=True)
    image = models.ImageField (upload_to='images')

    def __str__(self):
        return self.name