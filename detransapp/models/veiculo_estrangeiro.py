from django.db import models

from detransapp.models.tipo_veiculo import TipoVeiculo
from detransapp.models.cor import Cor
from detransapp.models.categoria import Categoria
from infracao import Infracao


class VeiculoEstrangeiro(models.Model):
    infracao = models.ForeignKey(Infracao)

    pais = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)

    placa = models.CharField(max_length=20, null=True)
    chassi = models.CharField(null=True, max_length=50)
    nr_motor = models.CharField(max_length=50, null=True)

    tipo_veiculo = models.ForeignKey(TipoVeiculo, null=True)

    cor = models.ForeignKey(Cor, null=True)
    categoria = models.ForeignKey(Categoria, null=True)
    ano_fabricacao = models.IntegerField(null=True)
    ano_modelo = models.IntegerField(null=True)
    num_passageiro = models.CharField(max_length=3, null=True)

    class Meta:
        app_label = "detransapp"
