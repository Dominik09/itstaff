# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0012_auto_20150730_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='', storage=django.core.files.storage.FileSystemStorage(location='/files/media')),
        ),
    ]
