# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 04:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0015_auto_20161011_0358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='template',
        ),
    ]
