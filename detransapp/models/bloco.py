from django.db import models
from django.contrib.auth.models import User

from detransapp.manager import BlocoManager


class Bloco(models.Model):
    inicio_intervalo = models.PositiveIntegerField()
    fim_intervalo = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)
    ativo = models.BooleanField(default=True)
    contador = models.IntegerField(default=0)

    objects = BlocoManager()
