# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enqueue', '0010_auto_20160209_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute_Value',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('value', models.CharField(max_length=4096, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engine_Attribute',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=4096, null=True)),
                ('engine', models.ForeignKey(to='enqueue.Engine')),
            ],
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='engine',
        ),
        migrations.DeleteModel(
            name='Attribute',
        ),
        migrations.AddField(
            model_name='attribute_value',
            name='engine_attribute',
            field=models.ForeignKey(to='enqueue.Engine_Attribute'),
        ),
    ]
