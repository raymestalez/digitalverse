# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-17 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20160917_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]