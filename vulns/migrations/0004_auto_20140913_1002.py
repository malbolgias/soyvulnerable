# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0003_auto_20140913_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerable',
            name='result',
            field=models.TextField(max_length=300),
        ),
    ]
