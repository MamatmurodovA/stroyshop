# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 23:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_product_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.VolumeType'),
        ),
    ]
