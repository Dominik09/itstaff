# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0002_auto_20150728_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
