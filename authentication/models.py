from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


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
    user_role = models.ForeignKey(Role, blank=True, null=True, default="1")
    class Meta:
        db_table = "user_profile"


class Phone(models.Model):
    type = models.CharField(max_length=40)

    class Meta:
        db_table = "phone"

    def __str__(self):
        return self.type


class UserPhone(models.Model):
    body = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, unique=False)

    class Meta:
        db_table = "user_phone"
