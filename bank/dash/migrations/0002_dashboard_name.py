# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='name',
            field=models.CharField(default='xyz', max_length=200),
        ),
    ]
