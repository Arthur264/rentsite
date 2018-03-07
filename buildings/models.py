from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db  import IntegrityError
# from mapwidgets.widgets import GooglePointFieldWidget
# Create your models here.


class House(models.Model):
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image_url = models.ImageField()
    price = models.IntegerField()
    bedrooms = models.SmallIntegerField(blank=True, null=True)
    bathrooms = models.SmallIntegerField(blank=True, null=True)
    area = models.SmallIntegerField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "house"

    # nice view
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(House, self).save(*args, **kwargs)


class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image_url = models.ImageField()

    class Meta:
        db_table = "houses_image"


class HouseDetails(models.Model):
    house = models.OneToOneField(House, unique=True)
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

    def add(self, uid, hid):
        try:
            visited = HouseVisited(user=uid, house=hid)
            visited.save()
            return True
        except IntegrityError:
            return False


