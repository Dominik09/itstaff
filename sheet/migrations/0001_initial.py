# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('com_text', models.TextField(verbose_name='Текст комментария:')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'sheet',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='com_sheet',
            field=models.ForeignKey(to='sheet.Sheet'),
        ),
    ]
