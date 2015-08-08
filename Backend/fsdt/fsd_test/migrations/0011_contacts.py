# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0010_delete_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=150)),
                ('mobile', models.BigIntegerField()),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('location', models.TextField()),
                ('last_dml_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
