# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vulnerable',
            name='date',
        ),
        migrations.RemoveField(
            model_name='vulnerable',
            name='ip_add',
        ),
        migrations.RemoveField(
            model_name='vulnerable',
            name='result',
        ),
    ]
