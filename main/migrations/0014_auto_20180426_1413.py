# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20180426_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticfooterpage',
            name='user_type',
            field=models.CharField(blank=True, choices=[(('clients', 'For clients'), ('partners', 'For partners'))], max_length=12, null=True),
        ),
    ]
