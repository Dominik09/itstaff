# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0005_auto_20150714_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolios',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('screenshot', models.ImageField(verbose_name='Скриншот', upload_to='')),
                ('about', models.TextField(verbose_name='Расскажите о проекте')),
                ('link', models.URLField(verbose_name='Ссылка на проект', blank=True, null=True)),
            ],
            options={
                'db_table': 'portfolios',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='clubs',
            field=models.CharField(verbose_name='Посещали ли вы кружки?', blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='university',
            field=models.CharField(verbose_name='Университет', blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='about_youself',
            field=models.TextField(verbose_name='Напишите о себе', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(verbose_name='Дата рождения', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=1, default='Пол', verbose_name='Пол', blank=True, choices=[('M', 'Мужчина'), ('F', 'Женщна')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='specialization',
            field=models.CharField(verbose_name='На чем вы специализируетесь?', blank=True, max_length=50, null=True),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
        migrations.AddField(
            model_name='portfolios',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
