# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170219_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='about'),
        ),
    ]