from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=40)
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    text = models.TextField()
    user_role = models.ForeignKey(Role)
    class Meta:
         db_table = "user_profile"
         
class Phone(models.Model):
    type = models.CharField(max_length= 40)


class UserPhone(models.Model):
    body = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    class Meta:
         db_table = "user_phone"

