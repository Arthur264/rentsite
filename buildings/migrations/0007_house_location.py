# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-10 16:05
from __future__ import unicode_literals

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0006_auto_20180310_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='location',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True),
        ),
    ]
