# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0005_agente_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloco',
            name='agente_campo',
            field=models.ForeignKey(related_name='+', blank=True, to='detransapp.Agente', null=True),
        ),
    ]
