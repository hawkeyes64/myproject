# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_auto_20161225_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='etab',
            name='tabs_icon',
            field=models.CharField(default='icon-file-text', max_length=100),
        ),
        migrations.AlterField(
            model_name='etab',
            name='tabs_anchor',
            field=models.CharField(max_length=51),
        ),
        migrations.AlterField(
            model_name='etab',
            name='tabs_text',
            field=models.CharField(max_length=50),
        ),
    ]
