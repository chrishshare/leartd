# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-25 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PMPDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_EN', models.CharField(max_length=50, verbose_name='英文全称')),
                ('long_CN', models.CharField(max_length=50, verbose_name='中文全称')),
                ('short', models.CharField(blank=True, max_length=10, null=True, verbose_name='英文缩写')),
                ('description', models.TextField(max_length=1000, verbose_name='术语解释')),
                ('version', models.CharField(blank=True, default='第五版', max_length=15, null=True, verbose_name='PMBOK版本')),
            ],
            options={
                'verbose_name': 'PMP术语',
                'verbose_name_plural': 'PMP术语',
            },
        ),
    ]
