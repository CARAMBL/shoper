from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.CharField (max_length=100)
    price = models.IntegerField()
    disc = models.CharField (max_length=500)

    def __str__(self):
        return self.name