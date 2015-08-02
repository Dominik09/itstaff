# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0009_auto_20150729_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='image',
            field=models.ImageField(blank=True, upload_to='/files/media/', null=True),
        ),
    ]
