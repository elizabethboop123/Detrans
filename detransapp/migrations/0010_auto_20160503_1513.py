# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0009_auto_20160502_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='DET',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='configsinc',
            old_name='horas_discarte',
            new_name='horas_descarte',
        ),
        migrations.AddField(
            model_name='infracao',
            name='det',
            field=models.CharField(default=b'0', max_length=255),
        ),
        migrations.AlterField(
            model_name='bloco',
            name='fim_intervalo',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='bloco',
            name='inicio_intervalo',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='codigo',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='cor',
            name='codigo',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='imei',
            field=models.CharField(unique=True, max_length=18),
        ),
        migrations.AlterField(
            model_name='especie',
            name='codigo',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='codigo',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='tipoveiculo',
            name='codigo',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='ano_fabricacao',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='ano_modelo',
            field=models.PositiveIntegerField(),
        ),
    ]
