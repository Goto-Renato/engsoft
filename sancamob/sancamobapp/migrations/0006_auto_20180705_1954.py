# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sancamobapp', '0005_auto_20180703_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rep',
            name='seguranca',
            field=models.IntegerField(default=0),
        ),
    ]
