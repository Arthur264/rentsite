# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-10 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_auto_20180307_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
