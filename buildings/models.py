from __future__ import unicode_literals
import datetime 
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class House(models.Model):
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image_url = models.ImageField()
    price = models.IntegerField()
    bedrooms = models.SmallIntegerField(blank=True, null=True, )
    bathrooms = models.SmallIntegerField(blank=True, null=True)
    area = models.SmallIntegerField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta: 
        db_table = "house"
        
    def __str__(self): #nice view
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(House, self).save(*args, **kwargs)
        



class HouseImage(models.Model):
    house = models.OneToOneField(House)
    title = models.CharField(max_length=200)
    image_url = models.ImageField()
    class Meta: 
        db_table = "houses_image"
    
  
  
class HouseDetails(models.Model):
    house = models.OneToOneField(House)
    text = models.TextField()
    garage = models.SmallIntegerField()
    class Meta: 
        db_table = "houses_details" 
