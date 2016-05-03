from django.db import models

from detransapp.manager import DispositivoManager


class Dispositivo(models.Model):
    # TODO Alterar para chave primaria
    imei = models.CharField(max_length=18,unique=True)
    ativo = models.BooleanField(default=True)

    objects = DispositivoManager()
