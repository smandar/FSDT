# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0014_delete_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=150, blank=True)),
                ('last_name', models.CharField(max_length=150, blank=True)),
                ('email_id', models.EmailField(max_length=150)),
                ('mobile', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('location', models.TextField(default=b'Not available')),
                ('last_dml_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
