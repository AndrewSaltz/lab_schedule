# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-24 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20170714_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='recurrences',
        ),
    ]
