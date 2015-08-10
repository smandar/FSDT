# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0012_auto_20150809_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='name',
        ),
        migrations.AddField(
            model_name='contacts',
            name='first_name',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='last_name',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
