# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-02 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_auto_20180301_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
    ]