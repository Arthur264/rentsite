# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-16 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0004_auto_20180216_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
