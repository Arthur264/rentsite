from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    create_date = models.DateTimeField('date created', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "news"


class NewsImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        db_table = "news_image"


class Comments(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=40)
    email = models.EmailField()
    website = models.CharField(max_length=100)
    create_date = models.DateTimeField('date created', auto_now=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"
