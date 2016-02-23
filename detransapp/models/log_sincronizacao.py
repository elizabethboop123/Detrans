# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

from detransapp.models import Dispositivo
from detransapp.manager import LogSincronizacaoManager


class LogSincronizacao(models.Model):
    dispositivo = models.ForeignKey(Dispositivo)
    usuario = models.ForeignKey(User)
    data = models.DateTimeField(auto_now_add=True)
    solicitacao = models.IntegerField(choices=((0, 'Download'), (1, 'Parcial'), (2, 'Recebimento infração')))

    objects = LogSincronizacaoManager()

    class Meta:
        app_label = "detransapp"
