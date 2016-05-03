# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0003_remove_blocopadrao_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocopadrao',
            name='numero_paginas',
            field=models.IntegerField(default=1000),
        ),
    ]
