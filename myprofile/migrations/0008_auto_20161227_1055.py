# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-27 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0007_auto_20161226_0051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme_link',
            old_name='about_me_icon',
            new_name='AboutMe_Link_icon',
        ),
        migrations.RenameField(
            model_name='aboutme_link',
            old_name='about_me_link',
            new_name='AboutMe_Link_link',
        ),
        migrations.RenameField(
            model_name='aboutme_link',
            old_name='about_me_user',
            new_name='AboutMe_Link_user',
        ),
    ]
