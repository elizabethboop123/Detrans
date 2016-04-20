# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0006_auto_20160331_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloco',
            name='fim_intervalo',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='bloco',
            name='inicio_intervalo',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='cor',
            name='codigo',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='especie',
            name='codigo',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='codigo',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
    ]
