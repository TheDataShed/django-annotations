# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enqueue', '0002_auto_20160204_1501'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Engine',
        ),
    ]
