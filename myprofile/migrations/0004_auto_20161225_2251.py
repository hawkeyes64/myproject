# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0003_auto_20161225_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme',
            old_name='about_me_facebook',
            new_name='about_me_email',
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='about_me_github',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='about_me_linkedin',
            field=models.CharField(default='#', max_length=100),
        ),
    ]
