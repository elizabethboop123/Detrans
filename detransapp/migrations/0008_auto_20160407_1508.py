# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0007_auto_20160407_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlocoPadrao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inicio_intervalo', models.IntegerField()),
                ('fim_intervalo', models.IntegerField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('contador', models.IntegerField(default=0)),
                ('ativo', models.BooleanField(default=True)),
                ('numero_paginas', models.IntegerField(default=1000)),
                ('minimo_pag_restantes', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bloco',
            name='contador',
        ),
        migrations.AddField(
            model_name='agente',
            name='cpf',
            field=models.CharField(default=b'12345678901', max_length=11),
        ),
        migrations.AddField(
            model_name='bloco',
            name='agente_campo',
            field=models.ForeignKey(related_name='+', blank=True, to='detransapp.Agente', null=True),
        ),
    ]
