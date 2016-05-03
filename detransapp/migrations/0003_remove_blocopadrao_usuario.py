# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0002_blocopadrao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blocopadrao',
            name='usuario',
        ),
    ]
