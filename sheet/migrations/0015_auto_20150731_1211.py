# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sheet.models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0014_auto_20150731_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to="files/"),
        ),
    ]
