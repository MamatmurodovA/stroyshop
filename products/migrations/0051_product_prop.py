# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-14 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0050_auto_20180614_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Property'),
        ),
    ]
