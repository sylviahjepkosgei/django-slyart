# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-23 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slypixels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
    ]
