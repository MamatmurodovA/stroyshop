# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.TextField(null=True),
        ),
    ]