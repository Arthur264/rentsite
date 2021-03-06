from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gismodel
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db  import IntegrityError
import datetime
# from location_field.models.plain import PlainLocationField
# from mapwidgets.widgets import GooglePointFieldWidget
# Create your models here.


class House(models.Model):
    FORRENT = 'FR'
    FORSILE = 'RS'
    STATUS_CHOICES = (
        (FORRENT, 'For Rent'),
        (FORSILE, 'For Sale')
    )
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image_url = models.ImageField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=FORRENT)
    price = models.IntegerField()
    bedrooms = models.SmallIntegerField(blank=True, null=True)
    bathrooms = models.SmallIntegerField(blank=True, null=True)
    area = models.SmallIntegerField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(User, related_name='house', on_delete=models.CASCADE)

    class Meta:
        db_table = "house"

    # nice view
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(House, self).save(*args, **kwargs)
        
    def get_favoriets(self):
        result = HouseFavorites.objects.filter(house_id=int(self.id)).values_list('user_id', flat=True)
        return result


class HouseImage(models.Model):
    house = models.ForeignKey(House, related_name='houseimage', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image_url = models.ImageField()

    class Meta:
        db_table = "houses_image"


class HouseDetails(models.Model):
    house = models.OneToOneField(House,  related_name='housedetails', unique=True)
    text = models.TextField()
    garage = models.SmallIntegerField()
    year_built = models.DateField()
    video = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'houses_details'


class HouseVisited(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'house')
        db_table = 'houses_visited'



class HouseLocation(models.Model):
    house = models.OneToOneField(House,  related_name='houselocation', unique=True)
    location = gismodel.PointField(blank=True, null=True)

    class Meta:
        db_table = 'location'


class HouseFavorites(models.Model):
    user = models.ForeignKey(User, related_name='housefavorites', on_delete=models.CASCADE)
    house = models.ForeignKey(House, related_name='housefavorites', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'house')
        db_table = "house_favorites"
