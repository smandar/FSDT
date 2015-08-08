# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsd_test', '0003_auto_20150808_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='myUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email_id', models.CharField(max_length=150)),
                ('mobile', models.BigIntegerField()),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
