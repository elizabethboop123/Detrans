# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0006_det'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='imei',
            field=models.CharField(unique=True, max_length=18),
        ),
    ]
