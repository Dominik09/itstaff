# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateTimeField()),
                ('specialization', models.CharField(max_length=50)),
                ('about_youself', models.TextField(verbose_name='Напишите о себе')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
