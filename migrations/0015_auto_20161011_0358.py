# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 03:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0014_auto_20161011_0347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='left_sidebar',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='right_sidebar',
        ),
        migrations.DeleteModel(
            name='LeftSidebar',
        ),
        migrations.DeleteModel(
            name='RightSidebar',
        ),
    ]