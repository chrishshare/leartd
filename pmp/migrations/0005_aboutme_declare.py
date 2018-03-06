# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-28 20:48
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmp', '0004_auto_20180226_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo', verbose_name='头像')),
                ('peer', models.CharField(max_length=100, verbose_name='职业')),
                ('email', models.EmailField(max_length=254, verbose_name='电子邮箱')),
                ('summary', ckeditor.fields.RichTextField(max_length=2000, verbose_name='简介')),
                ('createdate', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('lastupdate', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '关于我',
                'verbose_name_plural': '关于我',
            },
        ),
        migrations.CreateModel(
            name='Declare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(max_length=2000, verbose_name='申明内容')),
                ('createdate', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('lastupdate', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('wechar', models.ImageField(upload_to='wechar', verbose_name='微信收款码')),
                ('zifubao', models.ImageField(upload_to='zhifubao', verbose_name='支付宝收款码')),
            ],
            options={
                'verbose_name': '申明',
                'verbose_name_plural': '申明',
            },
        ),
    ]
