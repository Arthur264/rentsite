# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-15 19:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_auto_20180315_1908'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfavorites',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='userfavorites',
            name='house',
        ),
        migrations.RemoveField(
            model_name='userfavorites',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserFavorites',
        ),
    ]
