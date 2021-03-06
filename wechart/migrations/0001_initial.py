# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-07 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WXDevInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AppId', models.CharField(max_length=20, verbose_name='开发者ID(AppID)')),
                ('AppSecret', models.CharField(max_length=50, verbose_name='开发者密码(AppSecret)')),
                ('accesstoken', models.CharField(max_length=256, verbose_name='ACCESSTOKEN')),
            ],
            options={
                'verbose_name': '微信公众号基本信息',
                'verbose_name_plural': '微信公众号基本信息',
            },
        ),
    ]
