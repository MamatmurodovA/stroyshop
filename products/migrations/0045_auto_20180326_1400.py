# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-26 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0044_auto_20180326_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_0',
            field=models.ImageField(null=True, upload_to='products/', verbose_name='First image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_1',
            field=models.ImageField(null=True, upload_to='products/', verbose_name='Second image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(null=True, upload_to='products/', verbose_name='Third image'),
        ),
    ]
