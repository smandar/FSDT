# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email_id', models.CharField(max_length=150)),
                ('mobile', models.IntegerField()),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('location', models.TextField()),
            ],
        ),
    ]
