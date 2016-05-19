# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0012_auto_20160509_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrator',
            name='cnh',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='cnh',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
