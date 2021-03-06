# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-13 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0009_auto_20180412_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catCode', models.IntegerField()),
                ('catDescription', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='commodities',
            field=models.ManyToManyField(to='user_account.category'),
        ),
    ]
