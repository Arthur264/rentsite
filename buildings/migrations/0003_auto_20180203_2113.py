# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-03 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0002_auto_20180203_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='area',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='bathrooms',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='bedrooms',
            field=models.IntegerField(blank=True),
        ),
    ]
