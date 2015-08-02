# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0003_sheet_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sheet',
            old_name='photo',
            new_name='image',
        ),
    ]
