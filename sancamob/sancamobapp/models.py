# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Rep(models.Model):
    nome = models.TextField(max_length=80)
    endereco = models.TextField()
    vagas = models.IntegerField(default=0)
    valor = models.FloatField()
    descricao = models.TextField()
    mobiliado = models.BooleanField(default=False)
    garagem = models.BooleanField(default=False)
    seguranca = models.BooleanField(default=False)
    entrada_prox = models.TextField(max_length=10)
    fotos = models.ImageField(upload_to='images')


