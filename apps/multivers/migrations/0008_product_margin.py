# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multivers', '0007_auto_20170203_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='margin',
            field=models.IntegerField(choices=[(0, 'No margin'), (1, 'Has margin')], default=1),
        ),
    ]