# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-09 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0005_usercategories'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='commodities',
            field=models.ManyToManyField(to='user_account.userCategories'),
        ),
    ]
