# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0013_auto_20160509_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id_image', models.IntegerField(serialize=False, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'')),
                ('infracao_id', models.ForeignKey(to='detransapp.Infracao')),
            ],
        ),
    ]
