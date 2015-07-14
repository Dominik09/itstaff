# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_auto_20150713_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='Введите пароль', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='Введите login', max_length=20),
        ),
    ]
