# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0002_auto_20160204_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infracao',
            name='obs',
            field=models.TextField(null=True, blank=True),
        ),
    ]
