# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='validar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Local', models.ForeignKey(verbose_name=b'Local', to='niveis.Local', null=True)),
                ('Nome', models.ForeignKey(verbose_name=b'Pessoa', to='niveis.Pessoa', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
