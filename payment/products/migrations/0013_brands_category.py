# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-27 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20180224_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
