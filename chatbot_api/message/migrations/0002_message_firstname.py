# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='firstname',
            field=models.CharField(default='anonymous', max_length=128),
        ),
    ]