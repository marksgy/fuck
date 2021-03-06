# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('reply_channel', models.CharField(max_length=32)),
                ('online', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_provider', models.CharField(max_length=32)),
                ('customer', models.CharField(max_length=32)),
            ],
        ),
    ]
