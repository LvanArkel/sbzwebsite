# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multivers', '0006_auto_20170203_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='no_discount',
            field=models.IntegerField(choices=[(0, 'No discount'), (1, 'Discount if exclusive'), (2, 'Always discount')], null=True),
        ),
    ]
