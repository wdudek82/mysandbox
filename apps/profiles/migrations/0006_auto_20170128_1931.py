# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 18:31
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_color2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='color2',
        ),
        migrations.AlterField(
            model_name='profile',
            name='color',
            field=colorfield.fields.ColorField(max_length=10),
        ),
    ]