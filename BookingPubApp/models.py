from statistics import mode
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    thumbnail = models.CharField(max_length=100) #thumbnail of the restaurant, should be placed in the static folder
    images = models.CharField(max_length=500) #the images used for model prediction

    def __str__(self) -> str:
        return self.name