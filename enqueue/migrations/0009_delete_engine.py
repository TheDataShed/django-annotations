# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enqueue', '0008_engine'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Engine',
        ),
    ]
