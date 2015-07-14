# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='date',
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(verbose_name='Текст комментария:'),
        ),
    ]
