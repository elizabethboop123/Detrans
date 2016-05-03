# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0010_auto_20160503_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='ano_fabricacao',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
