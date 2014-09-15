# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0005_auto_20140914_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerable',
            name='date',
            field=models.DateTimeField(verbose_name=b'Fecha de prueba'),
        ),
    ]
