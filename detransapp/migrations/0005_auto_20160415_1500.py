# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0004_blocopadrao_numero_paginas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configsinc',
            name='horas_discarte',
        ),
        migrations.AddField(
            model_name='configsinc',
            name='horas_descarte',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='infracao',
            name='det',
            field=models.CharField(default=b'0', max_length=255),
        ),
    ]
