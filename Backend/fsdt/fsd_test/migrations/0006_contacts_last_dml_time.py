# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0005_auto_20150808_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='last_dml_time',
            field=models.TimeField(default=datetime.datetime(2015, 8, 8, 15, 9, 17, 775231, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
