# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 18:07
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170128_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='color',
            field=colorful.fields.RGBColorField(default='#000'),
        ),
    ]
