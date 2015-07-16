# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0008_remove_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='', verbose_name='Скриншот')),
                ('about', models.TextField(verbose_name='Расскажите о проекте')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка на проект')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'portfolio',
            },
        ),
        migrations.RemoveField(
            model_name='portfolios',
            name='user',
        ),
        migrations.DeleteModel(
            name='Portfolios',
        ),
    ]
