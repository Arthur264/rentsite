# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-12 17:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180312_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='name',
            new_name='author',
        ),
    ]