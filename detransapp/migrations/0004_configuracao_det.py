# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0003_auto_20160204_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracao_DET',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_registro', models.CharField(max_length=1)),
                ('formato', models.CharField(max_length=6)),
                ('cod_entidade', models.CharField(max_length=3)),
                ('entidade', models.CharField(max_length=40)),
                ('autuador', models.CharField(max_length=6)),
                ('tipo_arquivo', models.CharField(max_length=1)),
                ('filler', models.IntegerField()),
            ],
        ),
    ]
