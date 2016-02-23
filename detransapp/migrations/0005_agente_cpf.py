# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0004_configuracao_det'),
    ]

    operations = [
        migrations.AddField(
            model_name='agente',
            name='cpf',
            field=models.CharField(default=b'12345678901', max_length=11),
        ),
    ]
