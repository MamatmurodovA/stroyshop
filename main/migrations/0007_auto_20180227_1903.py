# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-27 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180227_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statictranslation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banners/%Y/%m/%d', verbose_name='Image'),
        ),
    ]
