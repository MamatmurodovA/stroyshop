# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180424_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticfooterpage',
            name='target_type',
            field=models.CharField(choices=[(('clients', 'For clients'), ('partners', 'For partners'))], default='clients', max_length=12),
        ),
    ]