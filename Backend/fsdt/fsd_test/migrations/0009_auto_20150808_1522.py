# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0008_auto_20150808_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='last_dml_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
