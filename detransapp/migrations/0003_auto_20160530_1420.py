# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrator',
            name='cnh',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='cnh',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
