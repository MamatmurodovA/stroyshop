# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-05 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20180303_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, unique=True, verbose_name='Phone number or Username'),
        ),
    ]
