# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-08 12:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
    ]