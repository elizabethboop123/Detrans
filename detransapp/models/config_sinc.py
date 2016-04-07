# coding: utf-8
from django.db import models

from detransapp.manager import ConfigSincManager


# TODO VALIDAR COM BRAZ, O GANHO DE DESEMPENHO
class ConfigSinc(models.Model):
    '''
    nr_dias_sem_sinc = models.IntegerField()
    is_execucao_importacao = models.BooleanField(default=False)

    # Intervalo onde pode ser inciado a sincronização
    hora_inicio_sinc = models.TimeField()
    hora_fim_sinc = models.TimeField()
'''

    horas_discarte = models.IntegerField()
    tempo_captura_mov = models.IntegerField()
    distancia_captura_mov = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)

    objects = ConfigSincManager()

    class Meta:
        app_label = "detransapp"
