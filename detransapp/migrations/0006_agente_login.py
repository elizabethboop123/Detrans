# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0005_auto_20160401_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agente_login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('data_login', models.DateTimeField(auto_now_add=True)),
                ('data_logout', models.DateTimeField(null=True, blank=True)),
                ('agente', models.ForeignKey(to='detransapp.Agente')),
                ('device', models.ForeignKey(to='detransapp.Dispositivo')),
            ],
        ),
    ]
