# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('enqueue', '0007_delete_engine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False)),
                ('name', models.CharField(max_length=4096)),
                ('power', models.CharField(max_length=4096)),
                ('cubic_capacity', models.CharField(max_length=4096)),
                ('torque', models.CharField(max_length=4096)),
                ('top_speed', models.CharField(max_length=4096)),
                ('acceleration', models.CharField(max_length=4096)),
                ('average_consumption', models.CharField(max_length=4096)),
                ('c02_emission', models.CharField(max_length=4096)),
                ('emission_category', models.CharField(max_length=4096)),
                ('start_stop_system', models.CharField(max_length=4096)),
            ],
        ),
    ]
