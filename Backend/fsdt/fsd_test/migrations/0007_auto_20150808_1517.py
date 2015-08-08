# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0006_contacts_last_dml_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email_id',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
