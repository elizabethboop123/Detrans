# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class LogImportacao(models.Model):
    nome_tabela = models.CharField(max_length=50)
    nome_arquivo = models.CharField(max_length=50)
    usuario = models.ForeignKey(User)
    data = models.DateTimeField(auto_now_add=True)
    data_execucao = models.DateTimeField(null=True)
    data_termino = models.DateTimeField(null=True)
    status = models.IntegerField(choices=((0, 'Aguardando'), (1, 'Executando'), (2, 'Falha'), (3, 'Sucesso')))
    msg_erro = models.TextField(null=True)

    class Meta:
        app_label = "detransapp"
