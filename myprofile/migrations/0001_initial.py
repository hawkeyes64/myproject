# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me_user', models.CharField(max_length=200)),
                ('about_me_general_role', models.CharField(max_length=200)),
                ('about_me_facebook', models.EmailField(default='#', max_length=254)),
                ('about_me_linkedin', models.EmailField(default='#', max_length=254)),
                ('about_me_github', models.EmailField(default='#', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CasualExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_label', models.CharField(max_length=30)),
                ('experience_date_from', models.CharField(max_length=4)),
                ('experience_date_to', models.CharField(max_length=4)),
                ('experience_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ETabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tabs_text', models.CharField(max_length=200)),
                ('tabs_anchor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='skill_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_type', models.CharField(max_length=20)),
                ('skill_text', models.CharField(max_length=100)),
                ('skill_bar_color', models.CharField(default='meter asbestos', max_length=30)),
                ('skill_bar_percent', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_label', models.CharField(max_length=30)),
                ('experience_date_from', models.CharField(max_length=4)),
                ('experience_date_to', models.CharField(max_length=4)),
                ('experience_description', models.CharField(max_length=200)),
            ],
        ),
    ]
