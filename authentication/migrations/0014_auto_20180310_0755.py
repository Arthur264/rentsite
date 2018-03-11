# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-10 07:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_userprofile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphone',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userphone', to=settings.AUTH_USER_MODEL),
        ),
    ]