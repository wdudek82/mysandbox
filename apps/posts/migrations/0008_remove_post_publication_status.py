# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170218_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publication_status',
        ),
    ]
