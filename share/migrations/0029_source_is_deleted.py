# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-11 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0028_auto_20170329_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
