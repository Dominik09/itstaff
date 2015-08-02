# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0008_auto_20150728_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
