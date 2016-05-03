# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0004_configuracao_det'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='codigo',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
    ]
