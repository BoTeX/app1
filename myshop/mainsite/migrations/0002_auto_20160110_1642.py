# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 14:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='email',
            field=models.CharField(max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(50), django.core.validators.MaxLengthValidator(200)]),
        ),
    ]
