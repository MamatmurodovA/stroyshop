# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20180301_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_recommended',
            field=models.BooleanField(default=False),
        ),
    ]
