# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-11 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]