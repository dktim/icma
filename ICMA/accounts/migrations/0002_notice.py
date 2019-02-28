# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-31 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(b'1', '\u5ba1\u6838')], max_length=5, null=True)),
                ('type_id', models.PositiveIntegerField()),
                ('user_id', models.PositiveIntegerField()),
                ('status', models.PositiveIntegerField(default=0, max_length=2, null=True)),
                ('adddate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]