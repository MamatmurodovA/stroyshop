# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_remove_product_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.VolumeType'),
        ),
    ]
