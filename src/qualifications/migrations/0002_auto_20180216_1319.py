# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-16 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='pass_date',
            field=models.DateField(),
        ),
    ]