from __future__ import unicode_literals
import datetime 
from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.IntegerField()
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self): #nice view
        return self.name



class Gallery(models.Model):
    house = models.ForeignKey(House)
    name = models.CharField(max_length=200)
    image = models.ImageField()