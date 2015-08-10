# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0013_auto_20150810_0352'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]
