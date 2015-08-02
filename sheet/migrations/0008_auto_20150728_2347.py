# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0007_auto_20150728_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to=''),
        ),
    ]
