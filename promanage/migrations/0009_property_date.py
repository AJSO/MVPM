# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-07 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promanage', '0008_auto_20170605_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]