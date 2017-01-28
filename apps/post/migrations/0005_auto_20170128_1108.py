# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 10:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20170128_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='deleted',
            new_name='archived',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='deleted_at',
            new_name='archived_at',
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
