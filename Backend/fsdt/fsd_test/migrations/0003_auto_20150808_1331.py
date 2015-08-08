# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0002_auto_20150808_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.BigIntegerField(max_length=10),
        ),
    ]
