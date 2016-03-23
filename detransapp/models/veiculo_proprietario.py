from django.db import models

from veiculo import Veiculo
from proprietario import Proprietario


class VeiculoProprietario(models.Model):
    veiculo = models.ForeignKey(Veiculo)
    proprietario = models.ForeignKey(Proprietario)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "detransapp"
