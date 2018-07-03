# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sancamobapp', '0004_rep_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rep',
            name='contato',
            field=models.TextField(max_length=250),
        ),
    ]
