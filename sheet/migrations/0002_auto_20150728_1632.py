# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='date',
            field=models.DateTimeField(default=0),
        ),
    ]
