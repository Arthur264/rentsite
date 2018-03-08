from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserMessage(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    message = models.TextField()
    email_user = models.EmailField()

    class Meta:
        db_table = 'user_message'
