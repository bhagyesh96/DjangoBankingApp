# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 05:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_auto_20170612_0517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carloan',
            old_name='key',
            new_name='dashboard',
        ),
    ]
