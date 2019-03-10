# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-03-02 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sdwan', '0006_classmodel_router_interface'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classmodel_router_interface',
            old_name='Interface_id',
            new_name='interface_id',
        ),
        migrations.RenameField(
            model_name='classmodel_router_interface',
            old_name='last_link_down_time',
            new_name='mgtIP',
        ),
        migrations.RenameField(
            model_name='classmodel_router_interface',
            old_name='last_link_up_time',
            new_name='password',
        ),
        migrations.AddField(
            model_name='classmodel_router_interface',
            name='username',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]