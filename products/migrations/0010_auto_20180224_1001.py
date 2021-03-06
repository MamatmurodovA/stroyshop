# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-24 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180222_2153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='categorytranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Category Translation'},
        ),
        migrations.AddField(
            model_name='variation',
            name='name',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
