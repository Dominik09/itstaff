# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0006_auto_20150728_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='image',
            field=models.ImageField(upload_to='', null=True),
        ),
    ]
