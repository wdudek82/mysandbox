# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_about_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ('-is_current',), 'verbose_name_plural': 'About'},
        ),
        migrations.RenameField(
            model_name='about',
            old_name='avatar',
            new_name='image',
        ),
    ]
