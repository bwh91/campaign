# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_auto_20161010_0630'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Header',
            new_name='Head',
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='header',
            new_name='head',
        ),
    ]
