# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-05 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchasemanager', '0002_auto_20190605_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='city',
        ),
        migrations.AddField(
            model_name='vendor',
            name='island',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='atoll',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
