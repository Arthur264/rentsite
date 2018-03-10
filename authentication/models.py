from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from buildings.models import House


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    avatar = models.ImageField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    slug = models.SlugField()
    user_role = models.ForeignKey(Role, blank=True, null=True, default="1")

    class Meta:
        db_table = "user_profile"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.first_name + "-" + self.user.lat_name)
        super(UserProfile, self).save(*args, **kwargs)


class Phone(models.Model):
    type = models.CharField(max_length=40)

    class Meta:
        db_table = "phone"

    def __str__(self):
        return self.type


class UserPhone(models.Model):
    body = models.CharField(max_length=40)
    user = models.ForeignKey(User, related_name='userphone', on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, unique=False)

    class Meta:
        db_table = "user_phone"


class UserFavorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'house')
        db_table = "user_favorites"
