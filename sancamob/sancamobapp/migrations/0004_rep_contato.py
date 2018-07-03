# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sancamobapp', '0003_auto_20180701_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='rep',
            name='contato',
            field=models.TextField(default=datetime.datetime(2018, 7, 3, 17, 38, 1, 609091, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
