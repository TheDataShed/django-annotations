# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('enqueue', '0009_delete_engine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=4096, null=True)),
                ('value', models.CharField(max_length=4096, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False)),
                ('name', models.CharField(max_length=4096, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='engine',
            field=models.ForeignKey(to='enqueue.Engine'),
        ),
    ]
