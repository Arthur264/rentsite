# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-24 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0002_auto_20180220_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='housedetails',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]