# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0003_auto_20150713_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.CharField(choices=[('UN', 'Unverificated'), ('NEW', 'Newbie'), ('SP', 'Specialist')], default='UN', max_length=3),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщна')], default='Пол', max_length=1),
        ),
    ]
