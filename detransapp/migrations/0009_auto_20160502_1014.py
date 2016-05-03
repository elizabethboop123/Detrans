# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0008_auto_20160407_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infracao',
            name='agente',
            field=models.ForeignKey(to='detransapp.Agente', null=True),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='dispositivo',
            field=models.ForeignKey(to='detransapp.Dispositivo', null=True),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='local',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='local_numero',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='tipo_infracao',
            field=models.ForeignKey(to='detransapp.TipoInfracao', null=True),
        ),
    ]
