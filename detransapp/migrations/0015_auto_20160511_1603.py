# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detransapp', '0014_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='infracao_id',
            new_name='infracao',
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
