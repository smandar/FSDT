# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0004_auto_20150808_1445'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='myUsers',
            new_name='Contacts',
        ),
    ]
