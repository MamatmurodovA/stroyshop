# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 07:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_variation_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='name',
        ),
    ]
