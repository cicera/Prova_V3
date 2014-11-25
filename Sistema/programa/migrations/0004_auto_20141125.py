# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0003_auto_20141125'),
    ]

    operations = [
        migrations.AddField(
            model_name='validar',
            name='Entrada',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='validar',
            name='Saida',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
    ]
