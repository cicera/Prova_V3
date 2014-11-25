# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0002_validar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='validar',
            old_name='Local',
            new_name='Descricao',
        ),
    ]
