# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-01 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import promanage.models


class Migration(migrations.Migration):

    dependencies = [
        ('promanage', '0020_rentalapplication_is_responded'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=promanage.models.notification_file_location),
        ),
        migrations.AddField(
            model_name='notification',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=promanage.models.notification_file_location),
        ),
    ]