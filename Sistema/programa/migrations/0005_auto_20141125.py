# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0004_auto_20141125'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='validar',
            unique_together=set([('Nome', 'Descricao')]),
        ),
    ]
