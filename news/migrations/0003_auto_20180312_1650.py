# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-12 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180311_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='body',
            new_name='comment',
        ),
    ]
