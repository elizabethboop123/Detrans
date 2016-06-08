# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0003_auto_20160530_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrator',
            name='documento',
            field=models.CharField(max_length=25, serialize=False, primary_key=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='documento',
            field=models.CharField(max_length=25, serialize=False, primary_key=True, db_index=True),
        ),
    ]
