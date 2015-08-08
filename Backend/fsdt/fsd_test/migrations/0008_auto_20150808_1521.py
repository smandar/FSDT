# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0007_auto_20150808_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='last_dml_time',
            field=models.TimeField(default=datetime.datetime(2015, 8, 8, 15, 21, 28, 804970, tzinfo=utc)),
        ),
    ]
