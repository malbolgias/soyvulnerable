# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0006_auto_20140914_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulnerable',
            name='city',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vulnerable',
            name='country',
            field=models.CharField(default=b'CO', max_length=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vulnerable',
            name='result',
            field=models.TextField(default=b'N/A', max_length=300),
        ),
    ]
