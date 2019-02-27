# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-27 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Model_Model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('router_name', models.CharField(max_length=60, unique=True)),
                ('mgtIP', models.CharField(max_length=60)),
                ('version', models.CharField(max_length=60)),
                ('cpu', models.CharField(max_length=60)),
                ('cpu_frequency', models.CharField(max_length=60)),
                ('architecture_name', models.CharField(max_length=60)),
                ('board_name', models.CharField(max_length=60)),
                ('alive', models.CharField(max_length=60)),
            ],
        ),
    ]
