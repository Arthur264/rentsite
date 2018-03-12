from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    create_date = models.DateTimeField('date created', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "news"
        verbose_name = "News"
        verbose_name_plural = "News"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)


class NewsImage(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        db_table = "news_image"

    def __str__(self):
        return self.image.name


class Comments(models.Model):
    comment = models.TextField()
    author = models.CharField(max_length=40)
    email = models.EmailField()
    website = models.CharField(max_length=100)
    create_date = models.DateTimeField('date created', auto_now=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.author
