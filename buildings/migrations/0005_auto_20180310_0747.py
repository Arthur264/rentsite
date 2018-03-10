# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-10 07:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0004_auto_20180310_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housedetails',
            name='house',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='housedetails', to='buildings.House'),
        ),
    ]
