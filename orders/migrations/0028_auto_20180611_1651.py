# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-11 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_auto_20180601_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Товары в корзине', 'verbose_name_plural': 'Товары в корзине'},
        ),
    ]
