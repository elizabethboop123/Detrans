# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0007_auto_20160331_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='ano_fabricacao',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='ano_modelo',
            field=models.PositiveIntegerField(),
        ),
    ]
