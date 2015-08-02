# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0005_auto_20150728_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
