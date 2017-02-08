# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-08 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_delete_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=70)),
                ('e_mail', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_submitted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
