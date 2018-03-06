# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-06 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20180305_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_role',
            field=models.ForeignKey(blank=True, default='Users', null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Role'),
        ),
    ]
