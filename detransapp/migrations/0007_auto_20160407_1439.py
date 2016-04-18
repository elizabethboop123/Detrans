# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0006_agente_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlocoPadrao',
        ),
        migrations.RemoveField(
            model_name='agente',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='bloco',
            name='agente_campo',
        ),
        migrations.AddField(
            model_name='bloco',
            name='contador',
            field=models.IntegerField(default=0),
        ),
    ]
