# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 15:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20170128_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desctiption',
            field=models.TextField(default=datetime.datetime(2017, 1, 28, 15, 9, 43, 35369, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='desctiption',
            field=models.TextField(default=datetime.datetime(2017, 1, 28, 15, 9, 48, 140034, tzinfo=utc)),
            preserve_default=False,
        ),
    ]