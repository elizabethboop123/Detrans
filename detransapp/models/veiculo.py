from django.db import models

from detransapp.manager import VeiculoManager
from detransapp.models.modelo import Modelo
from detransapp.models.tipo_veiculo import TipoVeiculo
from detransapp.models.especie import Especie
from detransapp.models.cidade import Cidade
from detransapp.models.cor import Cor
from detransapp.models.categoria import Categoria


class Veiculo(models.Model):
    chassi = models.CharField(primary_key=True, max_length=21)
    renavam = models.BigIntegerField()
    nr_motor = models.CharField(max_length=21)
    placa = models.CharField(max_length=7)
    modelo = models.ForeignKey(Modelo)
    tipo_veiculo = models.ForeignKey(TipoVeiculo)
    especie = models.ForeignKey(Especie)
    cidade = models.ForeignKey(Cidade)
    cor = models.ForeignKey(Cor)
    categoria = models.ForeignKey(Categoria)
    data = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)
    ano_fabricacao = models.PositiveIntegerField()
    ano_modelo = models.PositiveIntegerField()
    num_passageiro = models.CharField(max_length=3)
    # proprietario = models.ForeignKey(Proprietario)

    objects = VeiculoManager()

    class Meta:
        app_label = "detransapp"
