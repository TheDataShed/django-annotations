# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0005_auto_20160129_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
