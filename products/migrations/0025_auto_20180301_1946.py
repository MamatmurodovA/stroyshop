# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_product_available_in_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='available_in_stock',
            field=models.BooleanField(default=True, verbose_name='Available in stock'),
        ),
    ]
