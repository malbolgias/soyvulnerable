# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0004_auto_20140913_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulnerable',
            name='hostname',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vulnerable',
            name='vulnerable',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
