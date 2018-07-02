# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.TextField(max_length=80)),
                ('endereco', models.TextField()),
                ('vagas', models.IntegerField(default=0)),
                ('valor', models.FloatField()),
                ('descricao', models.TextField()),
                ('mobiliado', models.BooleanField(default=False)),
                ('garagem', models.BooleanField(default=False)),
                ('seguranca', models.BooleanField(default=False)),
                ('entrada_prox', models.TextField(max_length=10)),
                ('fotos', models.ImageField(upload_to='images')),
            ],
        ),
    ]
