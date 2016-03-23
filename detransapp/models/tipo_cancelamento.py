from django.db import models

from detransapp.manager import TipoCancelamentoManager


class TipoCancelamento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)

    objects = TipoCancelamentoManager()

    class Meta:
        app_label = "detransapp"
