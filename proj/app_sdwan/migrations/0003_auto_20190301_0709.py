# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-28 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sdwan', '0002_classmodel_router_register'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class_Model_Model1',
            new_name='ClassModel_Router_Basicinfo',
        ),
        migrations.AlterField(
            model_name='classmodel_router_register',
            name='routerip',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
