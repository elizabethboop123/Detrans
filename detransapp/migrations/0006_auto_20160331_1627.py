# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0005_auto_20160331_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoveiculo',
            name='codigo',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
    ]
