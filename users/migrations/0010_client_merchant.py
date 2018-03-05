# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-22 21:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180222_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_type', models.IntegerField(choices=[(1, 'Producer'), (2, 'Supplier')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='merchant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
