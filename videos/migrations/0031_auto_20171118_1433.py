# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0030_auto_20170927_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proj',
            name='image',
            field=models.CharField(default='/videos/default_proj.jpg', max_length=2000),
        ),
        migrations.AlterField(
            model_name='video',
            name='subtitles',
            field=models.CharField(default='/videos/empty.vtt', max_length=1000),
        ),
    ]