from django.db import models
from django.contrib.auth.models import User

from detransapp.manager import BlocoManager


class Bloco(models.Model):
    inicio_intervalo = models.IntegerField()
    fim_intervalo = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)
    ativo = models.BooleanField(default=True)
    contador = models.IntegerField(default=0)

    objects = BlocoManager()
