# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-01-30 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='status',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]