# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0011_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='location',
            field=models.TextField(default=b'Not available'),
        ),
    ]
