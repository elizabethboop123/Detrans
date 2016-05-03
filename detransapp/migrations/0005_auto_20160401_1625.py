# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0004_blocopadrao_numero_paginas'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloco',
            name='minimo_pag_restantes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='blocopadrao',
            name='minimo_pag_restantes',
            field=models.IntegerField(null=True),
        ),
    ]
