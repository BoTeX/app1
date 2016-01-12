# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 01:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_auto_20160111_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(50), django.core.validators.MaxLengthValidator(500)]),
        ),
    ]
