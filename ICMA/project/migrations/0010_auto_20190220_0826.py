# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-02-20 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_subtask_charge_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='sub_task',
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.task', verbose_name='\u6240\u5c5e\u4efb\u52a1'),
        ),
    ]
