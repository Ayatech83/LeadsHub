# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-12 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0007_auto_20180412_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='commodities',
        ),
    ]
