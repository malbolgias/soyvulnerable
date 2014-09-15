# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0002_auto_20140913_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulnerable',
            name='date',
            field=models.DateTimeField(default=datetime.date(2014, 9, 13), verbose_name=b'date checked'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vulnerable',
            name='ip_add',
            field=models.CharField(default='127.0.0.1', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vulnerable',
            name='port',
            field=models.CharField(default='8000', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vulnerable',
            name='result',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
    ]
